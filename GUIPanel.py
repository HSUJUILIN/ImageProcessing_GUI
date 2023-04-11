''' Import packages '''
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

# ''' Functions and Variables '''
default_dir = "D:/"


def ChooseImage():
    file_path = filedialog.askopenfilename(
        title=u'choose file', initialdir=(os.path.expanduser(default_dir)), filetypes=(("png files", "*.png"), ("tif files", "*.tif"),  ("all files", "*.*")))
    # img = ImageTk.PhotoImage(Image.open(file_path))
    image = Image.open(file_path)
    if (image.size[0] >= image.size[1]):
        image.thumbnail((100, 100/image.size[0]*image.size[1]))
    elif (image.size[0] < image.size[1]):
        image.thumbnail((100/image.size[1]*image.size[0], 100))
    else:
        print('Where is your FXXKING IMAGE!!?')
    img = ImageTk.PhotoImage(image)
    SubSample.config(image=img)
    SubSample.image = img


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
window.config(bg='grey')
window.iconbitmap("D:/github/ImageProcessing_GUI/Figures/Icon.ico")


# Ticks (the ticks on the top of window)
# menu1 = tk.Menu(window)
# window.config(menu=menu1)

# Second Layer Ticks
# menu2 = tk.Menu(menu1, tearoff=0)
# menu2.add_command(label='Open...', command=ChooseImage)
# menu2.add_command(label='Save...', command=SaveFile)
# menu1.add_cascade(label='File', menu=menu2)

# Frames (put the widgets)
LeftTop_frame = tk.Frame(window, width=200, height=400)
LeftTop_frame.place(x=5, y=5, height=400, width=200)
LeftBottom_frame = tk.Frame(window, width=200, height=180)
LeftBottom_frame.place(x=5, y=410, height=165, width=200)

Right_frame = tk.Frame(window, width=550, height=580)
Right_frame.place(x=210, y=5, height=570, width=600)

# Labels (put the text or image)
SubSample_title = tk.Label(LeftTop_frame, text='Basic Tools')
SubSample_title.place(y=0, width=180)
SubSample = tk.Label(LeftTop_frame)
SubSample.place(x=40, y=50, height=100, width=100)

# file_path = filedialog.askopenfilename(
#     title=u'choose file', initialdir=(os.path.expanduser(default_dir)), filetypes=(("png files", "*.png"), ("tif files", "*.tif"),  ("all files", "*.*")))
# img = ImageTk.PhotoImage(Image.open(file_path))
# SubSample = tk.Label(LeftTop_frame, image=img)
# SubSample.place(anchor='center', relx=0.5, rely=0.5)


# Buttons
Button_LoadImage = tk.Button(
    LeftTop_frame, text='Load...', command=ChooseImage)
Button_LoadImage.place(x=0, y=20)

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
