# source code: GUI app

import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox
import os

# main window settings
main_w = tkinter.Tk()
main_w.title("PEP8 auto-fixer")
# main_w.iconbitmap('icon_path')
main_w.geometry("450x400")
main_w.resizable(False,False)

# Frames
scroll_frame = tkinter.Frame(main_w)

# scrollable frame
scroll_bar = tkinter.Scrollbar(scroll_frame)
scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

text_area = tkinter.Text(scroll_frame, bg="SystemButtonFace")
text_area.pack()

text_area.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=text_area.yview)

scroll_frame.pack()

check_btn_vars = []

# functions 
def insert_check_btn(_range):
    for r in range(_range):
        var = tkinter.IntVar()
        check_btn_vars.append(var)
        check_btn = tkinter.Checkbutton(text_area, text=f'Item - {r}',
                                        variable=var,
                                        command=selection_get)
        text_area.window_create(tkinter.END, window=check_btn)
        text_area.insert(tkinter.END, "\n")
    text_area.configure(state=tkinter.DISABLED, cursor='')

selection = []
def selection_get():
    global selection
    selection = []
    for i in check_btn_vars:
        if i.get() == 1:
            selection.append(check_btn_vars.index(i))
    print(selection)

def browse_file():
    filetypes = (
        ('python files', '*.py'),
        ('All files', '*.*')
    )
    path = fd.askopenfilename(filetypes=filetypes)
    file_name = os.path.basename(path)
    file_label['text'] = file_name
    if len(file_name) != 0:
        check_button['state'] = tkinter.NORMAL

def message_info():
    messagebox.showinfo('Correct', 'This field has 5 characters')

# widgets
insert_check_btn(20)
file_button = tkinter.Button(main_w, text='Select file', command=browse_file)
file_button.place(x=10, y=10)
check_button = tkinter.Button(main_w, text='Check', command=message_info, state="disabled")
check_button.place(x=395, y=10)
file_label = tkinter.Label(main_w, text="", anchor="w", width=43, relief="sunken")
file_label.place(x = 80, y=13)

main_w.mainloop()
