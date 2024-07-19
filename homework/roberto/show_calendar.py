import tkinter as tk
import calendar
from datetime import datetime

class ShowCalendar(tk.Frame):
    """Class for showing a calendar in a Tkinter frame."""

    def __init__(self, master):
        """
        Initialize the ShowCalendar frame.

        :param master: The parent Tkinter widget.
        """
        super().__init__(master)
        self.master = master
        self.pack()

        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        self.header_frame = tk.Frame(self)
        self.header_frame.pack(side=tk.TOP, pady=10)

        self.calendar_frame = tk.Frame(self)
        self.calendar_frame.pack()

        self.create_widgets()
        self.show_calendar(self.current_year, self.current_month)

        # Create the context menu
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Create Meeting", command=self.create_meeting)
        self.context_menu.add_command(label="Create Event", command=self.create_event)

    def create_widgets(self):
        """Create the widgets for navigating and displaying the calendar."""
        self.prev_button = tk.Button(self.header_frame, text="<", command=self.prev_month)
        self.prev_button.grid(row=0, column=0)

        self.next_button = tk.Button(self.header_frame, text=">", command=self.next_month)
        self.next_button.grid(row=0, column=4)

        self.month_year_label = tk.Label(self.header_frame, text="")
        self.month_year_label.grid(row=0, column=1, columnspan=3)

        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day in enumerate(days):
            tk.Label(self.calendar_frame, text=day).grid(row=1, column=i)

    def show_calendar(self, year, month):
        """
        Display the calendar for a given year and month.

        :param year: The year to display.
        :param month: The month to display.
        """
        self.clear_calendar()
        cal = calendar.Calendar(firstweekday=6)
        month_days = cal.monthdayscalendar(year, month)

        self.month_year_label.config(text=f"{calendar.month_name[month]} {year}")

        for i, week in enumerate(month_days):
            for j, day in enumerate(week):
                if day != 0:
                    btn = tk.Button(self.calendar_frame, text=str(day))
                    btn.grid(row=i + 2, column=j)
                    btn.bind("<Button-1>", self.show_day_details)  # Bind left-click to show day details
                    btn.bind("<Button-3>", self.show_context_menu)  # Bind right-click to show context menu
                else:
                    tk.Button(self.calendar_frame, text=" ").grid(row=i + 2, column=j)

    def clear_calendar(self):
        """Clear the current calendar from the display."""
        self.calendar_frame.destroy()
        self.calendar_frame = tk.Frame(self)
        self.calendar_frame.pack()

    def prev_month(self):
        """Show the previous month."""
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.show_calendar(self.current_year, self.current_month)

    def next_month(self):
        """Show the next month."""
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.show_calendar(self.current_year, self.current_month)

    def show_day_details(self, event):
        """Display details of meetings and events for the selected date."""
        selected_day = event.widget.cget("text")
        selected_date = f"{self.current_year}-{self.current_month}-{selected_day}"

        # Read meetings and events from file for the selected date
        meetings = []
        events = []
        with open("meetings.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line.startswith("Meeting:") or line.startswith("Event:"):
                    if i + 5 < len(lines):  # Check if there are enough lines remaining
                        date_line = lines[i + 1].strip()
                        if date_line == f"Date: {selected_date}":
                            entry = {
                                "type": line.split(":")[0],
                                "name": line.split(":")[1].strip(),
                                "date": date_line.split(":")[1].strip(),
                                "hour_interval": lines[i + 2].strip().split(":")[1].strip(),
                                "access_level": lines[i + 3].strip().split(":")[1].strip(),
                                "usernames": lines[i + 4].strip().split(":")[1].strip(),
                                "importance": lines[i + 5].strip().split(":")[1].strip()
                            }
                            if line.startswith("Meeting:"):
                                meetings.append(entry)
                            elif line.startswith("Event:"):
                                events.append(entry)
                            i += 5  # Skip next 5 lines as we have captured all details for this meeting/event
                        else:
                            i += 1  # Move to the next line if date doesn't match
                    else:
                        i += 1  # Move to the next line if there aren't enough lines remaining
                else:
                    i += 1  # Move to the next line if it's not a Meeting or Event

        # Display details in a new window
        new_window = tk.Toplevel(self.master)
        new_window.title(f"Details for {selected_date}")

        if meetings:
            tk.Label(new_window, text="Meetings:").pack()
            for meeting in meetings:
                self.display_entry_details(new_window, meeting)
            tk.Label(new_window, text="").pack()  # Spacer
        else:
            tk.Label(new_window, text="No meetings found").pack()

        if events:
            tk.Label(new_window, text="Events:").pack()
            for event in events:
                self.display_entry_details(new_window, event)
        else:
            tk.Label(new_window, text="No events found").pack()

    def display_entry_details(self, window, entry):
        """Helper function to display details of a meeting or event in a window."""
        tk.Label(window, text=f"{entry['type']}: {entry['name']}").pack()
        tk.Label(window, text=f"Date: {entry['date']}").pack()
        tk.Label(window, text=f"Hour Interval: {entry['hour_interval']}").pack()
        tk.Label(window, text=f"Access Level: {entry['access_level']}").pack()
        tk.Label(window, text=f"Usernames: {entry['usernames']}").pack()
        tk.Label(window, text=f"Importance: {entry['importance']}").pack()
        tk.Label(window, text="").pack()  # Spacer

    def show_context_menu(self, event):
        """Display the context menu."""
        self.context_menu.post(event.x_root, event.y_root)
        self.selected_day = event.widget.cget("text")  # Store the selected day for further actions

    def create_meeting(self):
        """Create a meeting on the selected day."""
        self.open_meeting_frame("Create Meeting")

    def create_event(self):
        """Create an event on the selected day."""
        self.open_event_frame("Create Event")

    def open_meeting_frame(self, title):
        """Open a new frame to create a meeting with the given title."""
        new_window = tk.Toplevel(self.master)
        new_window.title(title)

        tk.Label(new_window, text=title, font=("Helvetica", 16)).pack(pady=20)
        tk.Label(new_window, text=f"Selected Date: {self.current_year}-{self.current_month}-{self.selected_day}").pack(
            pady=10)

        tk.Label(new_window, text="Meeting Name:").pack()
        meeting_name_entry = tk.Entry(new_window)
        meeting_name_entry.pack()

        tk.Label(new_window, text="Hour Interval (e.g., 10:00-11:00):").pack()
        hour_interval_entry = tk.Entry(new_window)
        hour_interval_entry.pack()

        tk.Label(new_window, text="Access Level:").pack()
        access_level_var = tk.StringVar(value="Everyone")
        access_everyone_rb = tk.Radiobutton(new_window, text="Everyone", variable=access_level_var, value="Everyone")
        access_everyone_rb.pack()
        access_private_rb = tk.Radiobutton(new_window, text="Private", variable=access_level_var, value="Private")
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
        importance_optional_rb = tk.Radiobutton(new_window, text="Optional", variable=importance_var, value="Optional")
        importance_optional_rb.pack()
        importance_important_rb = tk.Radiobutton(new_window, text="Important", variable=importance_var,
                                                 value="Important")
        importance_important_rb.pack()

        def save_meeting():
            selected_date = f"{self.current_year}-{self.current_month}-{self.selected_day}"
            meeting_name = meeting_name_entry.get()
            hour_interval = hour_interval_entry.get()
            access_level = access_level_var.get()
            usernames = usernames_entry.get() if access_level == "Private" else "Everyone"
            importance = importance_var.get()

            # Write meeting details to file
            with open("meetings.txt", "a") as file:
                file.write(f"Meeting: {meeting_name}\n")
                file.write(f"Date: {selected_date}\n")
                file.write(f"Hour Interval: {hour_interval}\n")
                file.write(f"Access Level: {access_level}\n")
                file.write(f"Usernames: {usernames}\n")
                file.write(f"Importance: {importance}\n\n")

            new_window.destroy()

        tk.Button(new_window, text="Save Meeting", command=save_meeting).pack(pady=20)
        tk.Button(new_window, text="Close", command=new_window.destroy).pack(pady=5)

    def open_event_frame(self, title):
        """Open a new frame to create an event with the given title."""
        new_window = tk.Toplevel(self.master)
        new_window.title(title)

        tk.Label(new_window, text=title, font=("Helvetica", 16)).pack(pady=20)
        tk.Label(new_window, text=f"Selected Date: {self.current_year}-{self.current_month}-{self.selected_day}").pack(
            pady=10)

        tk.Label(new_window, text="Event Name:").pack()
        event_name_entry = tk.Entry(new_window)
        event_name_entry.pack()

        tk.Label(new_window, text="Hour Interval (e.g., 10:00-11:00):").pack()
        hour_interval_entry = tk.Entry(new_window)
        hour_interval_entry.pack()

        def save_event():
            selected_date = f"{self.current_year}-{self.current_month}-{self.selected_day}"
            event_name = event_name_entry.get()
            hour_interval = hour_interval_entry.get()

            # Write event details to file
            with open("meetings.txt", "a") as file:
                file.write(f"Event: {event_name}\n")
                file.write(f"Date: {selected_date}\n")
                file.write(f"Hour Interval: {hour_interval}\n\n")

            new_window.destroy()

        tk.Button(new_window, text="Save Event", command=save_event).pack(pady=20)
        tk.Button(new_window, text="Close", command=new_window.destroy).pack(pady=20)

