"""Menu Page class"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from send_mail_page import SendMailPage
from show_calendar import ShowCalendar

class MenuPage(tk.Frame):
    """
    This is the MenuPage class with its methods.
    """
    title = "ScheduleSync"

    def __init__(self, master):
        """
        Initialize the MenuPage frame.
        """
        super().__init__(master)
        self.master = master
        self.master.title(self.title)
        self.pack()
        self.add_menu()
        tk.Label(self, text="What are the plans for today?", font=("Helvetica", 20)).pack(pady=30)

    def add_menu(self):
        """
        Add menu items to the menu bar.
        """
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
        menu_l2_1.add_command(label="LogOut", command=self.exit_app)

        menu_l2_2.add_command(label="Today's Meeting", command=self.show_meeting)
        menu_l2_2.add_separator()
        menu_l2_2.add_command(label="Create Meeting", command=self.create_meeting)
        menu_l2_2.add_separator()
        menu_l2_2.add_command(label="LogOut", command=self.exit_app)

        menu_l2_3.add_command(label="Show Calendar", command=self.show_calendar)
        menu_l2_3.add_separator()
        menu_l2_3.add_command(label="LogOut", command=self.exit_app)

    def create_meeting(self):#pylint: disable=too-many-locals
        #pylint: disable=too-many-statements
        """
        Open a new frame for creating a meeting.
        """
        title = "Create Meeting"
        new_window = tk.Toplevel(self.master)
        new_window.title(title)

        tk.Label(new_window, text=title, font=("Helvetica", 16)).pack(pady=20)

        tk.Label(new_window, text="Select Date:").pack()

        today = datetime.today()

        day_spinbox = tk.Spinbox(new_window, from_=1, to=31, width=5)
        day_spinbox.pack()

        month_spinbox = tk.Spinbox(new_window, from_=1, to=12, width=5)
        month_spinbox.pack()

        year_spinbox = tk.Spinbox(new_window, from_=today.year, to=today.year+10, width=5)
        year_spinbox.pack()

        tk.Label(new_window, text="Meeting Name:").pack()
        meeting_name_entry = tk.Entry(new_window)
        meeting_name_entry.pack()

        tk.Label(new_window, text="Hour Interval (e.g., 10:00-20:00):").pack()
        hour_interval_entry = tk.Entry(new_window)
        hour_interval_entry.pack()

        tk.Label(new_window, text="Access Level:").pack()
        access_level_var = tk.StringVar(value="Everyone")
        access_everyone_rb = tk.Radiobutton(new_window,
                                            text="Everyone",
                                            variable=access_level_var, value="Everyone")
        access_everyone_rb.pack()
        access_private_rb = tk.Radiobutton(new_window, text="Private",
                                           variable=access_level_var, value="Private")
        access_private_rb.pack()

        usernames_label = tk.Label(new_window, text="Usernames (comma-separated):")
        usernames_entry = tk.Entry(new_window)

        def toggle_usernames_entry():
            if access_level_var.get() == "Private":
                usernames_label.pack()
                usernames_entry.pack()
            else:
                usernames_label.pack_forget()
                usernames_entry.pack_forget()

        access_private_rb.config(command=toggle_usernames_entry)
        access_everyone_rb.config(command=toggle_usernames_entry)

        tk.Label(new_window, text="Importance:").pack()
        importance_var = tk.StringVar(value="Optional")
        importance_optional_rb = tk.Radiobutton(new_window,
                                                text="Optional",
                                                variable=importance_var, value="Optional")
        importance_optional_rb.pack()
        importance_important_rb = tk.Radiobutton(new_window,
                                                 text="Important", variable=importance_var,
                                                 value="Important")
        importance_important_rb.pack()

        def save_meeting():
            selected_date = f"{year_spinbox.get()}-{month_spinbox.get()}-{day_spinbox.get()}"
            meeting_name = meeting_name_entry.get()
            hour_interval = hour_interval_entry.get()
            access_level = access_level_var.get()
            usernames = usernames_entry.get() if access_level == "Private" else "Everyone"
            importance = importance_var.get()

            # Write meeting details to file
            with open("meetings.txt", "a", encoding='utf-8') as file:
                file.write(f"Meeting: {meeting_name}\n")
                file.write(f"Date: {selected_date}\n")
                file.write(f"Hour Interval: {hour_interval}\n")
                file.write(f"Access Level: {access_level}\n")
                file.write(f"Usernames: {usernames}\n")
                file.write(f"Importance: {importance}\n\n")

            print(f"Meeting saved: {meeting_name} on {selected_date} at {hour_interval} "
                  f"({access_level}, {usernames}, {importance})")
            new_window.destroy()

        tk.Button(new_window, text="Save Meeting", command=save_meeting).pack(pady=20)
        tk.Button(new_window, text="Close", command=new_window.destroy).pack(pady=5)

    def show_meeting(self):
        """
        Show today's meetings or display a message if there are none.
        """
        today = datetime.today().strftime('%Y-%m-%d')
        meetings_today = []

        # Read meetings from the file and check for today's meetings
        try:
            with open("meetings.txt", "r", encoding='utf-8') as file:
                lines = file.readlines()

            current_meeting = {}
            for line in lines:
                if line.strip() == "":
                    if current_meeting and current_meeting.get("Date") == today:
                        meetings_today.append(current_meeting)
                    current_meeting = {}
                else:
                    key, value = line.split(": ", 1)
                    current_meeting[key] = value.strip()

            if current_meeting and current_meeting.get("Date") == today:
                meetings_today.append(current_meeting)

        except FileNotFoundError:
            messagebox.showinfo("No Meetings/Events", "Today there are no meetings!")

        if meetings_today:
            new_window = tk.Toplevel(self.master)
            new_window.title("Today's Meetings/Events")

            for meeting in meetings_today:
                tk.Label(new_window, text=f"Meeting: {meeting.get('Meeting')}").pack()
                tk.Label(new_window, text=f"Date: {meeting.get('Date')}").pack()
                tk.Label(new_window, text=f"Hour Interval: {meeting.get('Hour Interval')}").pack()
                tk.Label(new_window, text=f"Access Level: {meeting.get('Access Level')}").pack()
                tk.Label(new_window, text=f"Usernames: {meeting.get('Usernames')}").pack()
                tk.Label(new_window, text=f"Importance: {meeting.get('Importance')}").pack()
                tk.Label(new_window, text="").pack()  # Add a blank line for spacing
        else:
            messagebox.showinfo("No Meetings/Events", "Today there are no meetings!")

    def send_mail(self):
        """
        This is the send mail method.
        """
        self.master.switch_frame(SendMailPage)

    def print_file(self):
        """
        This method is used to print some details.
        """
        print("Printing")

    def exit_app(self):
        """
        This method is used to exit the application.
        """
        self.master.destroy()

    def show_calendar(self):
        """
        This method is used to show the calendar.
        """
        self.master.switch_frame(ShowCalendar)
