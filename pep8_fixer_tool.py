# source code: GUI app

import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox
import os

# main window settings
main_w = tkinter.Tk()
main_w.title("PEP8 auto-fixer")
# main_w.iconbitmap('icon_path')
main_w.geometry("455x400")
main_w.resizable(False,False)

# scrollable frame
scroll_frame = tkinter.Frame(main_w)
scroll_bar = tkinter.Scrollbar(scroll_frame)
scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

text_area = tkinter.Text(scroll_frame,
                         bg="SystemButtonFace",
                         width=53,
                         height=20)
text_area.pack()
text_area.configure(yscrollcommand=scroll_bar.set)

scroll_bar.configure(command=text_area.yview)
scroll_frame.place(x=10,y=40)

# functions 
check_btn_vars = []
# it will store all the codes from the pep8 validation
rules = ['E271','E272','E273','E274','E401','E402']
def insert_check_btn(rules):
    for item_rule in rules:
        var = tkinter.IntVar()
        check_btn_vars.append(var)
        check_btn = tkinter.Checkbutton(text_area, 
                                        text=f'{item_rule} violation',
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
    print(selection) # debug

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
    messagebox.showinfo('Correct', 'This is just to test the check button')

def select_all():
    global check_btn_vars
    for item in check_btn_vars:
        item.set(1)
    # update the selection list
    selection_get()

# widgets
insert_check_btn(rules) # debug
select_button = tkinter.Button(main_w, text='Select all', command=select_all, state="disabled")
select_button.place(x=10, y=368)
fix_button = tkinter.Button(main_w, text='Fix!', state="disabled")
fix_button.place(x=410, y=368)
file_button = tkinter.Button(main_w, text='Select file', command=browse_file)
file_button.place(x=10, y=10)
check_button = tkinter.Button(main_w, text='Check', command=message_info, state="disabled")
check_button.place(x=395, y=10)
file_label = tkinter.Label(main_w, text="", anchor="w", width=43, relief="sunken")
file_label.place(x = 80, y=13)

main_w.mainloop()
