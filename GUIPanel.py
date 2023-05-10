''' Import packages '''
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog, ttk, messagebox

# ''' Functions and Variables '''
default_dir = "D:/"
StateCount = 0


def ChooseImage():
    global file_path
    file_path = filedialog.askopenfilename(
        title=u'choose file', initialdir=(os.path.expanduser(default_dir)), filetypes=(("png files", "*.png"), ("tif files", "*.tif"),  ("all files", "*.*")))
    filename = os.path.basename(file_path)
    ori_image = Image.open(file_path)
    ori_image_ = Image.open(file_path)
    info = f"File Name: {filename}\nWidth, Height: {ori_image.width}px, {ori_image.height}px\nBits: {ori_image.getbands()}\nFormat: {ori_image.format}\n"
    InfoSample.config(text=info)

    if (ori_image.size[0] >= ori_image.size[1]):
        ori_image.thumbnail((140, 140/ori_image.size[0]*ori_image.size[1]))
    elif (ori_image.size[0] < ori_image.size[1]):
        ori_image.thumbnail((140/ori_image.size[1]*ori_image.size[0], 140))
    else:
        pass

    img = ImageTk.PhotoImage(ori_image)
    SubSample.config(image=img)
    SubSample.image = img

    if (ori_image_.size[0] > 550 and ori_image_.size[1] <= 580):
        ori_image_.thumbnail((550, 550/ori_image_.size[0]*ori_image_.size[1]))
    elif (ori_image_.size[0] <= 550 and ori_image_.size[1] > 580):
        ori_image_.thumbnail((580/ori_image_.size[1]*ori_image_.size[0], 580))
    elif (ori_image_.size[0] > 550 and ori_image_.size[1] > 580):

        if (ori_image_.size[0]/550 > ori_image_.size[1]/580):
            ori_image_.thumbnail(
                (550, 550/ori_image_.size[0]*ori_image_.size[1]))
        elif (ori_image_.size[0]/550 < ori_image_.size[1]/580):
            ori_image_.thumbnail(
                (580/ori_image_.size[1]*ori_image_.size[0], 580))
        else:
            pass
    else:
        pass

    img = ImageTk.PhotoImage(ori_image_)
    Sample.config(image=img)
    Sample.image = img
    Text_StateWindow.insert(tk.END, "Loading image...\n")
    Text_StateWindow.see(tk.END)

    # def clear():
    #     height.set("")
    #     width.set("")


# def test1():
#     global StateCount

#     Text_StateWindow.insert(tk.END, "test1\n")
#     Text_StateWindow.see(tk.END)
    # StateCount += 1


# def test2():
#     global StateCount

#     Text_StateWindow.insert(tk.END, "test2\n")
#     Text_StateWindow.see(tk.END)
#     StateCount += 1


def Quit():
    Messagebox_Quit = messagebox.askquestion(
        'WARNING...', 'Are you sure you want to quit the GUI programe?', icon='warning')
    if (Messagebox_Quit == 'yes'):
        window.destroy()
    else:
        messagebox.showinfo('RETURN', 'You will return the main window.')


def Tutorial():
    Tutorial = tk.Toplevel(window)
    Tutorial.title('Tutorial')
    Tutorial.geometry('500x500')
    Text_Tutorial = tk.Text(Tutorial)
    Text_Tutorial.place(x=5, y=5, width=490, height=490)
    tutorialfile = "ImageProcessing_GUI/Tutorial.txt"
    with open(tutorialfile, 'r') as f:
        Text_Tutorial.insert(tk.INSERT, f.read())
    Text_Tutorial.config(state=tk.DISABLED)


def RGB2GRAY():
    print('Tida!!')


def ThresholdBar(CheckBox_Threshold_State):
    print(CheckBox_Threshold_State.get())
    # if (CheckBox_Threshold_State.get() == 'ON'):
    # ThresholdValue = ScaleBar_Threshold.get()
    # print(ThresholdValue)
    # print('CCCCCCCC')
    # else:
    # pass


def SaveFile():
    print('Saving...')


def DumpFile():
    print('Dumping...')


''' Main Programme '''

if __name__ == "__main__":
    # Windows Constructure
    window = tk.Tk()
    window.title('Image Processing GUI')
    window.geometry('800x600')
    window.resizable(True, True)
    window.config(bg='grey')

    # Ticks (the ticks on the top of window)
    menu1 = tk.Menu(window)
    window.config(menu=menu1)

    # Second Layer Ticks
    File_menu2 = tk.Menu(menu1, tearoff=0)
    File_menu2.add_command(label='Open...')
    File_menu2.add_command(label='Save...')
    menu1.add_cascade(label='File', menu=File_menu2)

    Window_menu2 = tk.Menu(menu1, tearoff=0)
    Window_menu2.add_command(label='Tutorial', command=Tutorial)
    Window_menu2.add_command(label='Quit', command=Quit)
    menu1.add_cascade(label='Window', menu=Window_menu2)

    # Frames (put the widgets)
    LeftTop_frame = tk.Frame(window)
    LeftTop_frame.place(x=5, y=5, height=400, width=200)
    LeftBottom_frame = tk.Frame(window)
    LeftBottom_frame.place(x=5, y=410, height=185, width=200)
    Right_frame = tk.Frame(window)
    Right_frame.place(x=210, y=5, height=590, width=585)

    # Labels (put the text or image)
    SubSample_title = tk.Label(
        LeftTop_frame, text='Image Information', font=("Arial", 15))
    SubSample_title.place(y=0, width=180)
    SubSample = tk.Label(LeftTop_frame)
    SubSample.place(x=20, y=70, height=140, width=140)
    InfoSample = tk.Label(LeftTop_frame, text="")
    InfoSample.place(x=100, y=250, anchor="center")
    Sample = tk.Label(Right_frame)
    Sample.place(x=20, y=2, height=580, width=550)
    Tools_title = tk.Label(
        LeftBottom_frame, text='Tools', font=("Arial", 15))
    Tools_title.place(y=0, width=180)
    # Threshold_title = tk.Label(LeftBottom_frame, text='Thresholds')
    # Threshold_title.place(x=5, y=60)
    Blur_title = tk.Label(LeftBottom_frame, text='Blur kernel size: ')
    Blur_title.place(x=5, y=125)
    Blur_unit = tk.Label(LeftBottom_frame, text='px')
    Blur_unit.place(x=125, y=125)

    # Buttons
    Button_LoadImage = tk.Button(
        LeftTop_frame, text='Load...', command=ChooseImage)
    Button_LoadImage.place(x=0, y=40)
    Button_Quit = tk.Button(LeftTop_frame, text='Quit',
                            command=Quit)
    Button_Quit.place(x=160, y=40)

    Button_RGB2GRAY = tk.Button(
        LeftBottom_frame, text='Grey', command=RGB2GRAY)
    Button_RGB2GRAY.place(x=5, y=30)

    # Entry
    Entry_Blur = tk.Entry(LeftBottom_frame)
    Entry_Blur.place(x=100, y=125, width=20)

    # CheckBoxes
    CheckBox_Threshold_State = tk.StringVar()
    CheckBox_Threshold = tk.Checkbutton(
        LeftBottom_frame, text='Threshold (scroll bar)', variable=CheckBox_Threshold_State, onvalue='ON', offvalue='OFF')
    CheckBox_Threshold.place(x=5, y=60)
    CheckBox_Threshold.deselect()

    # Texts
    Text_StateWindow = tk.Text(LeftTop_frame)
    Text_StateWindow.place(x=10, y=285, relwidth=0.9, height=110)

    # ScrollBars
    Bar_State = tk.Scrollbar(Text_StateWindow, orien='vertical',
                             command=Text_StateWindow.yview)
    Bar_State.pack(side=tk.RIGHT, fill='y')

    # Separators
    Separator1 = ttk.Separator(LeftTop_frame, orient='horizontal')
    Separator1.place(relx=0, y=280, relwidth=1, relheight=0.01)

    # Scales
    ScaleBar_Threshold = tk.Scale(
        LeftBottom_frame, from_=0, to=255, orient='horizontal', length=185, command=ThresholdBar(CheckBox_Threshold_State))
    ScaleBar_Threshold.place(x=5, y=80)

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
