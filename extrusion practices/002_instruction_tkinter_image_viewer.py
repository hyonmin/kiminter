from tkinter import *
from typing import Collection
from PIL import ImageTk, Image
import os

root =  Tk()
root.title("Image Viewer")
gom_path = os.getcwd()
gom_path = gom_path + "/gom.ico"
gom = ImageTk.PhotoImage(Image.open(gom_path))
root.iconphoto(False, gom)

img1 = ImageTk.PhotoImage(Image.open("photos/photo1.jpeg"))
img2 = ImageTk.PhotoImage(Image.open("photos/photo2.jpeg"))
img3 = ImageTk.PhotoImage(Image.open("photos/photo3.jpeg"))
img4 = ImageTk.PhotoImage(Image.open("photos/photo4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("photos/photo5.jpg"))

image_list = [img1, img2, img3, img4, img5]
my_label = Label(image = img1)
my_label.grid(row=2, column=0, columnspan=3)
# make a label look like a sunken down(bd and relief options)
status = Label(root, text = 'image 1 of ' + str(len(image_list)), bd=1, relief = SUNKEN)
status.grid(row=1, column=0, columnspan = 3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text = '>>', command = lambda: forward(image_number+1))
    button_back = Button(root, text = '<<', command = lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    
    status = Label(root, text = 'Image ' + str(image_number) + ' of ' + str(len(image_list)), bd=1, relief = SUNKEN)
    status.grid(row=1, column=0, columnspan = 3, sticky=W+E)
    button_back.grid(row=0, column=0)
    button_forward.grid(row=0, column=2)
    my_label.grid(row=2, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text = '>>', command = lambda: forward(image_number+1))
    button_back = Button(root, text = '<<', command = lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    status = Label(root, text = 'Image ' + str(image_number) + ' of ' + str(len(image_list)), bd=1, relief = SUNKEN)
    status.grid(row=1, column=0, columnspan = 3, sticky=W+E)
    button_back.grid(row=0, column=0)
    button_forward.grid(row=0, column=2)
    my_label.grid(row=2, column=0, columnspan=3)



button_back = Button(root, text = '<<', command = lambda: back, state=DISABLED)
button_exit = Button(root, text = 'EXIT PROGRAM', command=root.quit)
button_forward = Button(root, text = '>>', command = lambda: forward(2))

button_back.grid(row=0, column=0)
button_exit.grid(row=0, column=1)
button_forward.grid(row=0, column=2)


root.mainloop()