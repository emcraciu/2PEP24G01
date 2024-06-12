# TK menue
import tkinter


class App1():
    title = "Test Menu"

    def __init__(self, main_window: tkinter.Tk):
        self.main_window = main_window
        self.main_window.title(self.title)
        self.add_menu()

    def add_menu(self):
        menu_l1_1 = tkinter.Menu(self.main_window)
        self.main_window.config(menu=menu_l1_1)

        menu_l2_1 = tkinter.Menu(self.main_window)
        menu_l1_1.add_cascade(label="File", menu=menu_l2_1)

        menu_l2_2 = tkinter.Menu(self.main_window)
        menu_l1_1.add_cascade(label="Edit", menu=menu_l2_2)

        menu_l2_3 = tkinter.Menu(self.main_window)
        menu_l1_1.add_cascade(label="View", menu=menu_l2_3)

        menu_l2_1.add_command(label="Open", command=self.open_file)
        menu_l2_1.add_separator()
        menu_l2_1.add_command(label="Print", command=self.print_file)

    def open_file(self):
        print("opening file")

    def print_file(self):
        print("printing file")

    def run(self):
        self.main_window.mainloop()
        self.main_window.destroy()


window = tkinter.Tk()
app = App1(window)
app.run()
