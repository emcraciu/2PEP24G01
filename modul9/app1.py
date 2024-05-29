"""Create triangle from grid cels with some color"""

import tkinter as tk


class Triangle:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Triangle")
        self.main_window.grid_columnconfigure(index=0, minsize=500)

        for i in range(100):
            label1 = tk.Label(self.main_window, bg="red")
            label1.grid(row=i, column=0)
            label1.config(width=i * 3)

    def run(self):
        self.main_window.mainloop()
