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


def SaveFile():
    print('Saving...')


def DumpFile():
    print('Dumping...')


''' Main Programme '''

# Windows Constructure
window = tk.Tk()
window.title('GUI')
window.geometry('800x600')
window.resizable(True, True)
window.config(bg='black')
window.iconbitmap("D:/github/ImageProcessing_GUI/Figures/Icon.ico")


# Labels
menu1 = tk.Menu(window)
window.config(menu=menu1)

# Second Layer Labels
menu2 = tk.Menu(menu1, tearoff=0)
menu2.add_command(label='Open...', command=ChooseImage)
menu2.add_command(label='Save...', command=SaveFile)
menu1.add_cascade(label='File', menu=menu2)

# Frames
LeftTop_frame = tk.Frame(window, width=200, height=400)
LeftTop_frame.grid(row=0, column=0, padx=10, pady=5)

Right_frame = tk.Frame(window, width=550, height=400)
Right_frame.grid(row=0, column=1, padx=10, pady=5)


# Buttons
# Button_ = tk.Button(window)

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
