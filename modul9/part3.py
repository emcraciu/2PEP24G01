import tkinter


def clicked():
    print("You have clicked button")


main_window = tkinter.Tk()
main_window.title("MyApp")

button1 = tkinter.Button(main_window, text="Click Me", command=clicked)
button1.grid(row=0, column=1)

entry = tkinter.Entry(main_window, takefocus=True, bg="blue")
entry.grid(row=0, column=0)

text = tkinter.Text(main_window, takefocus=True, width=30)
text.grid(row=0, column=2)

main_window.mainloop()
