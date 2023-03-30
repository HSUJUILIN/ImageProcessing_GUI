''' Import packages '''
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

# ''' Functions and Variables '''
default_dir = "D:/"


def ChooseImage():
    file_path = filedialog.askopenfilename(
        title=u'choose file', initialdir=(os.path.expanduser(default_dir)), filetypes=(("png files", "*.png"), ("all files", "*.*")))
    img = ImageTk.PhotoImage(Image.open(file_path))
    frame.configure(image=img)
    frame.image = img


def SaveFile():
    print('Saving...')


def DumpFile():
    print('Dumping...')


def DisplayImage():
    file_path = filedialog.askopenfilename(
        title=u'choose file', initialdir=(os.path.expanduser(default_dir)), filetypes=(("png files", "*.png"), ("all files", "*.*")))
    img = ImageTk.PhotoImage(Image.open(file_path))
    frame.configure(image=img)
    frame.image = img


''' Main Programme '''

# Windows Constructure
window = tk.Tk()
window.title('GUI')
window.geometry('800x600')
window.resizable(True, True)
window.iconbitmap("D:/github/ImageProcessing_GUI/Figures/Icon.ico")

# Groups
# Group_panel = tk.LabelFrame(window, text='', width=770, height=570)
# Group_panel.place(x=10, y=300)
# Group_panel.pack()

Group_region1 = tk.LabelFrame(
    window, text='Basic function', width=200, height=320)
Group_region1.place(x=10, y=10)
Group_region1.pack()

Group_region2 = tk.LabelFrame(
    window, text='Advanced function', width=200, height=320)
Group_region1.place(x=300, y=340)
Group_region1.pack()

# Labels
menu1 = tk.Menu(window)
window.config(menu=menu1)

# Second Layer Labels
menu2 = tk.Menu(menu1, tearoff=0)
menu2.add_command(label='Open...', command=ChooseImage)
menu2.add_command(label='Save...', command=SaveFile)
menu1.add_cascade(label='File', menu=menu2)

# Buttons
Button_ = tk.Button(window)

window.mainloop()

# ''' Work Space '''


# def browse_image():
#     file_path = tk.filedialog.askopenfilename()
#     img = Image.open(file_path)
#     img = img.resize((250, 250), Image.LANCZOS)
#     img = ImageTk.PhotoImage(img)
#     panel.configure(image=img)
#     panel.image = img


# root = tk.Tk()
# root.title("Image Viewer")
# root.geometry("500x500")

# browse_button = tk.Button(root, text="Browse", command=browse_image)
# browse_button.pack()

# panel = tk.Label(root)
# panel.pack()

# root.mainloop()
