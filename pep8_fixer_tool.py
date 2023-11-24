#source code: GUI app

import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox
import os

# main window settings
main_w = tkinter.Tk()
main_w.title("PEP8 auto-fixer")
main_w.geometry("400x400")
main_w.resizable(False,False)

file_name = "--"

def open_text_file():
    filetypes = (
        ('python files', '*.py'),
        ('All files', '*.*')
    )
    path = fd.askopenfilename(filetypes=filetypes)
    global file_name
    file_name = os.path.basename(path)
    file_label.config(text = file_name)

def message_info():
    messagebox.showinfo('Correct', 'This field has 5 characters')

# widgets
file_button = tkinter.Button(main_w, text='Select file', command=open_text_file)
file_button.place(x=10, y=10)
check_button = tkinter.Button(main_w, text='Check', command=message_info)
check_button.place(x=10, y=40)
file_label = tkinter.Label(main_w, text=file_name, anchor="w", width=40, relief="sunken")
file_label.place(x = 80, y=13)

main_w.mainloop()
