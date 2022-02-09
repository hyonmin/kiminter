from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

r = Tk()
r.title("test")

def open():
    global img
    r.filename = filedialog.askopenfilename(initialdir='', title="Select A File", filetypes=(("ico files", "*.ico"), ("Python files", "*.py"), ("all files", "*.*")))
    label=Label(r, text = r.filename).pack()
    img = ImageTk.PhotoImage(Image.open(r.filename))
    image_label = Label(image=img).pack()

btn = Button(r, text = 'Open File', command = open).pack()

r.mainloop()

