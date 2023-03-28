# ''' Design the panel '''
# import tkinter as tk

# ''' Main Programme '''
# window = tk.Tk()
# window.title('GUI')
# window.geometry('360x480')
# window.resizable(True, True)
# window.iconbitmap('D:/github/ImageProcessing_GUI/Figures/Icon.bmp')


# def mouseevent


# window.mainloop()
from tkinter import *


def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return


master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text=whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>', motion)
msg.pack()
mainloop()
