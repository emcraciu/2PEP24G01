from tkinter import Tk
import webview

main_window = Tk()

main_window.geometry('1024x800')
main_window.title('Final Project App')

webview.create_window('my_app', 'http://localhost:8501/')

webview.start()

