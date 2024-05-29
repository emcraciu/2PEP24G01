"""Create triangle from grid cels with some color"""

import tkinter as tk

main_window = tk.Tk()
main_window.title("Triangle")
main_window.grid_columnconfigure(index=0, minsize=500)

for i in range(100):
    label1 = tk.Label(main_window, bg="red")
    label1.grid(row=i, column=0)
    label1.config(width=i*3)


main_window.mainloop()
