"""Main Menu page"""

import tkinter as tk
from Main_Page import MainPage

class MenuPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Menu", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self, text="Logout", command=lambda: master.switch_frame(MainPage)).pack(pady=10)
        # Add more widgets to the menu page as needed
