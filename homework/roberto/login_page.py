"""Login page class file"""

import tkinter as tk
from tkinter import messagebox
from menu_page import MenuPage

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

        username = self.entry1.get()
        password = self.entry2.get()

        if not self.check.get():
            messagebox.showinfo("Calendar", "You cannot login.")
            return

        if self.validate_credentials(username, password):
            messagebox.showinfo("Calendar", "Login success")
            self.master.switch_frame(MenuPage)
        else:
            messagebox.showinfo("Calendar", "Username or password incorrect")

    def validate_credentials(self, username, password):
        """
        Validate the username and password against the Accounts.txt file.
        :param username: The username to validate.
        :param password: The password to validate.
        :return: True if the credentials are valid, False otherwise.
        """
        try:
            with open("Accounts.txt", "r", encoding='utf-8') as file:
                accounts = file.read().split("-------------------------\n")
                for account in accounts:
                    account_details = account.split("\n")
                    account_i = {line.split(": ")[0]: line.split(": ")[1]
                                    for line in account_details if
                                    ": " in line}
                    if account_i.get("Username")==username and account_i.get("Password")==password:
                        return True
        except FileNotFoundError:
            messagebox.showinfo("Calendar", "Accounts file not found.")

        return False
