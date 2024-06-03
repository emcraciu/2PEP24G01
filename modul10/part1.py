import tkinter
import os
import tkinter.messagebox

text: tkinter.Text
entry1: tkinter.Entry
entry2: tkinter.Entry
entry3: tkinter.Entry
login_fail: bool
username: str
password: str

def send_email(username, password, message):


def send_message(sender="", receiver=""):
    global text, entry1, entry2, entry3
    message = text.get(0.0, tkinter.END)
    print(entry1.get())
    print(entry2.get())
    print(entry3.get())
    response = tkinter.messagebox.askquestion(title='Are you sure you want to send the email')
    if response == 'yes':
        send_email(username, password, message)


class SendMail(tkinter.Frame):
    def __init__(self, parent, main):
        tkinter.Frame.__init__(self, parent)
        for idx, value in enumerate(["Subject", "Sender", "Content"]):
            label = tkinter.Label(self, text=value)
            label.grid(row=0, column=idx)
        all_files = os.listdir(".")
        for file in all_files:
            if not file.endswith(".txt"):
                continue
            with open(file, "r") as open_email:
                content = open_email.read()
            content_label = tkinter.Label(self, text=content)
            content_label.grid(row=0, column=0)


class ComposeMail(tkinter.Frame):
    def __init__(self, parent, main):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Compose Mail")
        label.pack()
        self.text = tkinter.Text(self, width=30, height=15)
        self.text.pack()
        entry_label1 = tkinter.Label(self, text="From:")
        self.entry1 = tkinter.Entry(self)
        entry_label2 = tkinter.Label(self, text="To:")
        self.entry2 = tkinter.Entry(self)
        entry_label3 = tkinter.Label(self, text="Subject:")
        self.entry3 = tkinter.Entry(self)
        entry_label1.pack()
        self.entry1.pack()
        entry_label2.pack()
        self.entry2.pack()
        entry_label3.pack()
        self.entry3.pack()


class MailButtons(tkinter.Frame):
    def __init__(self, parent, main):
        tkinter.Frame.__init__(self, parent)
        buttons = {"Send Mail": send_message, "Get Mail": lambda: True, "Attach File": lambda: True,
                   "Cancel": lambda: True, "Edit": lambda: True}
        for btn_name, btn_func in buttons.items():
            btn = tkinter.Button(self, text=btn_name,
                                 command=btn_func)
            btn.pack()


class MainWindow(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("Mail Client")
        main_frame = tkinter.Frame(self, height=800, width=800)
        main_frame.pack()
        main_frame.grid_columnconfigure(0)
        main_frame.grid_rowconfigure(0)
        mail2 = ComposeMail(main_frame, self)
        global text
        text = mail2.text
        global entry1, entry2, entry3
        entry1, entry2, entry3 = mail2.entry1, mail2.entry2, mail2.entry3
        button = MailButtons(main_frame, self)
        button.grid(rowspan=2, column=0)
        mail1 = SendMail(main_frame, self)
        mail1.grid(row=1, column=1)
        mail2.grid(row=0, column=1)


class Login:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Login")

        label1 = tkinter.Label(self.main_window, text="Username:")
        label1.grid(row=0, column=0)
        label2 = tkinter.Label(self.main_window, text="Password:")
        label2.grid(row=1, column=0)

        self.entry1 = tkinter.Entry(self.main_window, takefocus=True)
        self.entry1.grid(row=0, column=1)
        self.entry2 = tkinter.Entry(self.main_window, takefocus=True)
        self.entry2.grid(row=1, column=1)

        button1 = tkinter.Button(self.main_window, text="Login", command=self.login)
        button1.grid(row=2, column=0)

        button2 = tkinter.Button(self.main_window, text="Cancel", command=self.main_window.quit)
        button2.grid(row=2, column=1)

        self.check = tkinter.IntVar()

        check_box = tkinter.Checkbutton(self.main_window, text="I am not a robot", variable=self.check)
        check_box.grid(row=3, column=0)

        self.text = tkinter.Text()

    def login(self):
        global username, password
        username = self.entry1.get()
        password = self.entry2.get()
        self.main_window.quit()

    def run(self):
        self.main_window.mainloop()
        self.main_window.destroy()


login = Login()
login.run()

MainWindow().mainloop()
