from tkinter import Tk
import webview
import subprocess
import csv

with open(r'C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\logfile.csv',
          'w', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(['funcname', 'starttime', 'endtime', 'executiontime'])

# cmd = ['streamlit', 'run', '.\\StockApp\\stock_app.py', '&']
cmd = ['streamlit', 'run', '.\\StockApp\\stock_app.py', '--server.headless', 'true']
process = subprocess.Popen(cmd, text=True, stdout=subprocess.PIPE)

cmd1 = ['python', '.\\StockApp\\data_server.py']
process1 = subprocess.Popen(cmd1, text=True, stdout=subprocess.PIPE)

main_window = Tk()
main_window.geometry('1024x800')
main_window.title('Final Project App')

webview.create_window('my_app', 'http://localhost:8501/')

webview.start()
process.kill()
process1.kill()
