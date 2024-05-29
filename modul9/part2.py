import tkinter

main_window = tkinter.Tk()
main_window.title("MyApp")
main_window.grid_columnconfigure(index=0, minsize=500)

label1 = tkinter.Label(main_window, text="RED TEXT", bg="red")
label1.grid(row=0, column=0)

label2 = tkinter.Label(main_window, text="BLUE TEXT", bg="blue")
label2.grid(row=1, column=1)
label2.config(width=100)

label3 = tkinter.Label(main_window, text="MAGENTA TEXT", bg="magenta")
label3.grid(row=22, column=22)
label3.config(font=("Times New Roman", 25))

label4 = tkinter.Label(main_window, text="YELLOW TEXT", bg="yellow")
label4.grid(row=33, column=33)

label5 = tkinter.Label(main_window, text="GREEN TEXT", bg="green")
label5.grid(row=44, column=44)

main_window.mainloop()
