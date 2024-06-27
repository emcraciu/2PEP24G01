"""Login page class file"""

import tkinter as tk
from tkinter import messagebox
from Main_Page import  MainPage



class LoginPage(tk.Frame):
    """
    This is the login class with its methods.
    """
    def __init__(self, master):
        super().__init__(master)
        self.login_try = 0
        tk.Label(self, text="Username:").grid(row=0, column=0)
        tk.Label(self, text="Password:").grid(row=1, column=0)

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=1)
        self.entry2 = tk.Entry(self, show='*')
        self.entry2.grid(row=1, column=1)

        tk.Button(self, text="Login", command=self.login).grid(row=2, column=0)
        tk.Button(self, text="Cancel",
                  command=lambda: master.switch_frame(MainPage)).grid(row=2, column=1)

        self.check = tk.IntVar()
        tk.Checkbutton(self, text="I am not a robot", variable=self.check).grid(row=3, column=0)

    def login(self):
        """
        This is the login function.
        :return:
        """
        if self.login_try < 2:
            self.login_try += 1
        else:
            self.master.quit()
        if self.entry1.get() == "Roberto" and self.entry2.get() == "1234":
            print("login success")
            self.master.switch_frame(MainPage)
        elif not self.check.get():
            messagebox.showinfo("Calendar", "You cannot login.")
        else:
            print("Login failed")




