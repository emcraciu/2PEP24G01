import tkinter


class SendMail(tkinter.Frame):
    def __init__(self, parent, main):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Send Mail")
        label.pack()

class CpomposeMail(tkinter.Frame):
    def __init__(self, parent, main):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Compose Mail")
        label.pack()

class MainWindow(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("MailClient")

        main_frame = tkinter.Frame(self, height=800, width=800)
        main_frame.pack()

        main_frame.grid_columnconfigure(0)
        main_frame.grid_rowconfigure(0)

        mail = SendMail(main_frame, self)
        mail.grid()
        mail = CpomposeMail(main_frame, self)
        mail.grid()



MainWindow().mainloop()
