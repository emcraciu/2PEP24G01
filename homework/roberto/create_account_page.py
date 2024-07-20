"""Create account class"""

import tkinter as tk
from tkinter import messagebox

class CreateAccountPage(tk.Frame):
    """
    This class creates a page for users to create an account.
    """

    def __init__(self, master):
        """
        Initialize the CreateAccountPage frame.
        """
        super().__init__(master)
        self.entries = {}
        labels = [
            "First Name:", "Last Name:", "Email:", "Phone number:",
            "Username:", "Password:", "Repeat password:"
        ]

        for idx, label_text in enumerate(labels):
            tk.Label(self, text=label_text).grid(row=idx, column=0)
            # pylint: disable=consider-using-in
            entry = tk.Entry(self, show='*' if label_text == "Password:" or
                                               label_text == "Repeat password:" else None)
            entry.grid(row=idx, column=1)
            self.entries[label_text] = entry

        tk.Button(self, text="Create", command=self.create_account).grid(row=len(labels), column=0)

        self.check = tk.IntVar()
        tk.Checkbutton(self, text="Accept terms and conditions.",
                       variable=self.check).grid(row=len(labels) + 1, column=0)

    def create_account(self):
        """
        Handle the creation of a new account.
        """
        if not self.check.get():
            messagebox.showinfo("Calendar", "You need to accept the terms and conditions.")
            return

        first_name = self.entries["First Name:"].get()
        last_name = self.entries["Last Name:"].get()
        email = self.entries["Email:"].get()
        phone_number = self.entries["Phone number:"].get()
        username = self.entries["Username:"].get()
        password = self.entries["Password:"].get()
        repeat_password = self.entries["Repeat password:"].get()

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
            "-------------------------"
        )

        with open("Accounts.txt", "a", encoding='utf-8') as file:
            file.write(account_details + "\n")

        messagebox.showinfo("Calendar", "Account created successfully.")
        self.master.quit()
