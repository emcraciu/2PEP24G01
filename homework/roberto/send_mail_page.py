import tkinter as tk
from tkinter import messagebox
from functools import partial
import os

class SendMailPage(tk.Frame):
    """
    This is the SendMailPage class with its methods.
    """
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        tk.Label(self, text="Send Mail", font=("Helvetica", 20)).pack(pady=10)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="From:").pack()
        self.from_entry = tk.Entry(self)
        self.from_entry.pack()


        tk.Label(self, text="To:").pack()
        self.to_entry = tk.Entry(self)
        self.to_entry.pack()

        tk.Label(self, text="Subject:").pack()
        self.subject_entry = tk.Entry(self)
        self.subject_entry.pack()

        tk.Label(self, text="Message:").pack()
        self.message_text = tk.Text(self, width=40, height=10)
        self.message_text.pack()

        tk.Button(self, text="Send", command=self.send_mail).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: self.master.switch_frame("MenuPage")).pack(pady=5)

    def send_mail(self):
        from_address = self.from_entry.get()
        to_address = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get(1.0, tk.END)
        print(f"Sending mail from {from_address} to {to_address} with subject {subject}")
        print(f"Message: {message}")
        tk.messagebox.showinfo("Mail Client", "Email sent successfully!")

