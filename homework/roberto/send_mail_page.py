"""Send mail page class file"""

import tkinter as tk

class SendMailPage(tk.Frame):
    """
    This is the SendMailPage class.
    """
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        tk.Label(self, text="Send Mail").pack(pady=10)
        tk.Label(self, text="Recipient:").pack()
        self.recipient_entry = tk.Entry(self)
        self.recipient_entry.pack()
        tk.Label(self, text="Subject:").pack()
        self.subject_entry = tk.Entry(self)
        self.subject_entry.pack()
        tk.Label(self, text="Message:").pack()
        self.message_entry = tk.Text(self, height=10, width=40)
        self.message_entry.pack()
        tk.Button(self, text="Send", command=self.send_mail).pack(pady=10)

    def send_mail(self):
        """
        This method is used to send the mail.
        :return:
        """
        recipient = self.recipient_entry.get()
        subject = self.subject_entry.get()
        message = self.message_entry.get("1.0", tk.END)

        with open("SentMails.txt", "a", encoding='utf-8') as file:
            file.write(f"To: {recipient}\nSubject: {subject}\nMessage: {message}\n-------------------------\n")

        tk.messagebox.showinfo("Mail", "Mail sent successfully.")
        self.master.switch_frame(self.master.previous_frame)
