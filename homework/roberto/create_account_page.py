import tkinter as tk
from tkinter import messagebox
import sqlite3

class CreateAccountPage(tk.Frame):
    """
    This is the CreateAccountPage class with its methods.
    """
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="First Name:").grid(row=0, column=0)
        tk.Label(self, text="Last Name:").grid(row=1, column=0)
        tk.Label(self, text="Email:").grid(row=2, column=0)
        tk.Label(self, text="Phone number:").grid(row=3, column=0)
        tk.Label(self, text="Username:").grid(row=4, column=0)
        tk.Label(self, text="Password:").grid(row=5, column=0)
        tk.Label(self, text="Repeat password:").grid(row=6, column=0)

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=1)
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=1)
        self.entry3 = tk.Entry(self)
        self.entry3.grid(row=2, column=1)
        self.entry4 = tk.Entry(self)
        self.entry4.grid(row=3, column=1)
        self.entry5 = tk.Entry(self)
        self.entry5.grid(row=4, column=1)
        self.entry6 = tk.Entry(self)
        self.entry6.grid(row=5, column=1)
        self.entry7 = tk.Entry(self, show='*')
        self.entry7.grid(row=6, column=1)

        tk.Button(self, text="Create", command=self.create_account).grid(row=7, column=0)

        self.check = tk.IntVar()
        tk.Checkbutton(self, text="Accept terms and conditions.", variable=self.check).grid(row=8, column=0)

    def create_account(self):
        """
        This is the create account function.
        :return:
        """
        if not self.check.get():
            messagebox.showinfo("Calendar", "You need to accept the terms and conditions.")
            return

        first_name = self.entry1.get()
        last_name = self.entry2.get()
        email = self.entry3.get()
        phone_number = self.entry4.get()
        username = self.entry5.get()
        password = self.entry6.get()
        repeat_password = self.entry7.get()

        if password != repeat_password:
            messagebox.showinfo("Calendar", "Passwords do not match.")
            return

        account_details = (
            f"First Name: {first_name}\n"
            f"Last Name: {last_name}\n"
            f"Email: {email}\n"
            f"Phone Number: {phone_number}\n"
            f"Username: {username}\n"
            f"Password: {password}\n"
            "-------------------------\n"
        )

        with open("Accounts.txt", "a", encoding='utf-8') as file:
            file.write(account_details)

        messagebox.showinfo("Calendar", "Account created successfully.")
        self.master.quit()

