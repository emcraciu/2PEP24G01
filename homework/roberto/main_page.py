"""Main page class file"""

import tkinter as tk
from tkinter import messagebox
from login_page import LoginPage
from create_account_page import CreateAccountPage

class MainPage(tk.Frame):
    """
    This is the main page class.
    """
    def __init__(self, master):
        super().__init__(master)
        title_label = tk.Label(self, text="Welcome to Your Calendar", font=("Helvetica", 16))
        title_label.pack(pady=20)

        login_button = tk.Button(self, text="Login", command=lambda: master.switch_frame(LoginPage))
        login_button.pack(pady=10)

        create_account_button = tk.Button(self, text="Create Account", command=lambda: master.switch_frame(CreateAccountPage))
        create_account_button.pack(pady=10)

        exit_button = tk.Button(self, text="Exit", command=self.exit_app)
        exit_button.pack(pady=10)

    def create_account(self):
        """
        This method is used to go to the create_account frame.
        :return:
        """
        messagebox.showinfo("Create Account", "This will open the create account window.")

    def exit_app(self):
        """
        This method is used to exit the application.
        :return:
        """
        self.master.destroy()
