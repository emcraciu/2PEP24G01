"""Main file to run the application"""

import tkinter as tk
from main_page import MainPage

class ScheduleSync(tk.Tk):
    """
    This is the App class.
    """
    def __init__(self):
        super().__init__()
        self.title("Calendar Application")
        self.geometry("400x300")
        self.current_frame = None
        self.switch_frame(MainPage)

    def switch_frame(self, frame_class):
        """
        This method switches the current frame to the new frame.
        :param frame_class: The new frame class.
        :return: None
        """
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()

if __name__ == "__main__":
    app = ScheduleSync()
    app.mainloop()
