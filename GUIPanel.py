''' Import packages '''
import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

''' Functions and Variables '''
default_dir = "D:/"


def ChooseFile():
    file_path = filedialog.askopenfilename(
        title=u'choose file', initialdir=(os.path.expanduser(default_dir)), filetypes=(("png files", "*.png"), ("all files", "*.*")))
    print(file_path)


def SaveFile():
    print('Saving...')


def DumpFile():
    print('Dumping...')


def DisplayImage():
    print('Display...')


''' Main Programme '''

# Windows Constructure
window = tk.Tk()
window.title('GUI')
window.geometry('800x600')
window.resizable(True, True)
window.iconbitmap("D:/github/ImageProcessing_GUI/Figures/Icon.ico")

# Frames
frame = tk.Frame(window, width=400, height=300)
frame.pack()
frame.place(x=200, y=50)


img = ImageTk.PhotoImage(Image.open(
    'D:/github/ImageProcessing_GUI/Figures/Icon.ico'))
label = tk.Label(frame, image=img)
label.pack()

# Labels
menu1 = tk.Menu(window)
window.config(menu=menu1)

# Second Layer Labels
menu2 = tk.Menu(menu1, tearoff=0)
menu2.add_command(label='Open...', command=ChooseFile)
menu2.add_command(label='Save...', command=SaveFile)
menu1.add_cascade(label='File', menu=menu2)

# Buttons
button_Display = tk.Button(text='Diaplay')
button_Display.place(x=0, y=0)
button_Display.pack()

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
