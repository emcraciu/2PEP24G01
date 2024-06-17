import tkinter


class App1():
    title = "Test Menu"

    def __init__(self, main_window: tkinter.Tk):
        self.main_window = main_window
        self.main_window.title(self.title)
        self.add_menu()
        self.add_text_area()

    def add_text_area(self):
        self.text_area = tkinter.Text(self.main_window, height=30, width=50)
        self.text_area.pack()

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
        with open('input.txt', 'r') as file:
            text = file.read()
        self.text_area.delete(0.0, tkinter.END)
        self.text_area.insert(0.0, text)

    def print_file(self):
        text = self.text_area.get(0.0, tkinter.END)
        print(text)

    def run(self):
        self.main_window.mainloop()
        self.main_window.destroy()


window = tkinter.Tk()
app = App1(window)
app.run()
