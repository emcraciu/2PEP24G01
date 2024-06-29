import tkinter as tk
from send_mail_page import SendMailPage

class MenuPage(tk.Frame):
    title = "ScheduleSync"

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title(self.title)
        self.pack()
        self.add_menu()
        tk.Label(self, text="What are the plans for today?", font=("Helvetica", 20)).pack(pady=30)

    def add_menu(self):
        menu_l1_1 = tk.Menu(self.master)
        self.master.config(menu=menu_l1_1)

        menu_l2_1 = tk.Menu(self.master)
        menu_l1_1.add_cascade(label="Mail", menu=menu_l2_1)

        menu_l2_2 = tk.Menu(self.master)
        menu_l1_1.add_cascade(label="Meetings", menu=menu_l2_2)

        menu_l2_3 = tk.Menu(self.master)
        menu_l1_1.add_cascade(label="MyCalendar", menu=menu_l2_3)

        menu_l2_1.add_command(label="Send Mail", command=self.send_mail)
        menu_l2_1.add_separator()
        menu_l2_1.add_command(label="Received Mails", command=self.print_file)
        menu_l2_1.add_separator()
        menu_l2_1.add_command(label="Sent Mails", command=self.print_file)
        menu_l2_1.add_separator()
        menu_l2_1.add_command(label="Important Mails", command=self.print_file)
        menu_l2_1.add_separator()
        menu_l2_1.add_command(label="All Mails", command=self.print_file)

        menu_l2_2.add_command(label="Create Meeting", command=self.print_file)
        menu_l2_2.add_separator()
        menu_l2_2.add_command(label="Show Meetings", command=self.print_file)
        menu_l2_2.add_separator()
        menu_l2_2.add_command(label="Delete Meeting", command=self.print_file)

        menu_l2_3.add_command(label="Show Calendar", command=self.print_file)

    def send_mail(self):
        self.master.switch_frame(SendMailPage)

    def print_file(self):
        pass

