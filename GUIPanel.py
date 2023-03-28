''' Import packages '''
import os
import tkinter as tk
from tkinter import filedialog

''' Functions and Variables '''
default_dir = "D:/"


def ChooseFile():
    file_path = filedialog.askopenfilename(
        title=u'choose file', initialdir=(os.path.expanduser(default_dir)))


''' Main Programme '''

# Windows Constructure
window = tk.Tk()
window.title('GUI')
window.geometry('360x480')
window.resizable(True, True)
window.iconbitmap("D:/github/ImageProcessing_GUI/Figures/Icon.bmp")

# Labels
menu = tk.Menu(window)
window.config(menu=menu)
menu.add_command(label='File', command=ChooseFile)

# Buttons
file_dir = tk.Button(text='OPEN...', command=ChooseFile)
file_dir.place(x=0, y=0)

window.mainloop()

# ''' Work Space '''
# from tkinter import *


# def motion(event):
#     print("Mouse position: (%s %s)" % (event.x, event.y))
#     return


# master = Tk()
# whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
# msg = Message(master, text=whatever_you_do)
# msg.config(bg='lightgreen', font=('times', 24, 'italic'))
# msg.bind('<Motion>', motion)
# msg.pack()
# mainloop()
