"""ScheduleSyncApp main"""

import tkinter as tk
from Main_Page import MainPage

class ScheduleSyncApp(tk.Tk):
    """
    ScheduleSyncApp class
    """
    def __init__(self):
        super().__init__()
        self.title("ScheduleSync")
        self.geometry("400x300")
        self._frame = None
        self.switch_frame(MainPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = ScheduleSyncApp()
    app.mainloop()



