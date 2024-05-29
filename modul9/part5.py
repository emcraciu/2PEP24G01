# Login APP

import tkinter
from modul9.app1 import Triangle

login_try = 0
login_fail = False


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
        global login_try
        if login_try < 2:
            login_try += 1
        else:
            global login_fail
            login_fail = True
        if self.entry1.get() == "admin" and self.entry2.get() == "test":
            self.main_window.quit()
            return
        if not self.check.get():
            self.text.grid(row=4, columnspan=3)
            self.text.config(width=30)

    def run(self):
        self.main_window.mainloop()


login = Login()
login.run()
if login_fail:
    quit()
# triangle = Triangle()
# triangle.run()
