# Login APP

import tkinter

login_try = 0


def login():
    global login_try
    if login_try < 2:
        login_try += 1
    else:
        main_window.quit()
    if entry1.get() == "admin" and entry2.get() == "test":
        print("login success")
    if not check.get():
        print("You are a robot")


main_window = tkinter.Tk()
main_window.title("Login")

label1 = tkinter.Label(main_window, text="Username:")
label1.grid(row=0, column=0)
label2 = tkinter.Label(main_window, text="Password:")
label2.grid(row=1, column=0)

entry1 = tkinter.Entry(main_window, takefocus=True)
entry1.grid(row=0, column=1)
entry2 = tkinter.Entry(main_window, takefocus=True)
entry2.grid(row=1, column=1)

button1 = tkinter.Button(main_window, text="Login", command=login)
button1.grid(row=2, column=0)

button2 = tkinter.Button(main_window, text="Cancel", command=main_window.quit)
button2.grid(row=2, column=1)

check = tkinter.IntVar()

check_box = tkinter.Checkbutton(main_window, text="I am not a robot", variable=check)
check_box.grid(row=3, column=0)

main_window.mainloop()
