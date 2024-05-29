import tkinter

main_window = tkinter.Tk()
main_window.title("MyApp")

label1 = tkinter.Label(main_window, text="RED TEXT", bg="red")
label1.pack(fill=tkinter.Y)
label2 = tkinter.Label(main_window, text="BLUE TEXT", bg="blue")
label2.pack(fill=tkinter.X)

label4 = tkinter.Label(main_window, text="MAGENTA TEXT", bg="magenta")
label4.pack(side=tkinter.LEFT, fill=tkinter.Y)

label5 = tkinter.Label(main_window, text="YELLOW TEXT", bg="yellow")
label5.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

label3 = tkinter.Label(main_window, text="GREEN TEXT", bg="green")
label3.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)

main_window.mainloop()
