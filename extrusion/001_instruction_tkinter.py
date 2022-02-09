from tkinter import *

# create a window, variable 'root' is the window.
root = Tk()
# create a label widget
mylabel1 = Label(root, text = 'hello world')
mylabel2 = Label(root, text = 'nobody knows')
# pack(), put a widget onto the screen
# mylabel1.pack()
# mylabel1.pack()

# grid()
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)

# function
def myClick():
    mylabel3 = Label(root, text="hey, do not click me!")
    mylabel3.grid()



# buttons, 'padx' and 'pady' options give some spaces to the both sides or up and down
# but 'height' and 'width' options give an absolute volume fixed of widgets.
# 'fg' and 'bg' options give colors to letters written in widgets
# and backgronds of widgets respectively.
# option 'bd': make the button being a depth visually.
mybutton1 = Button(root, text='do not click', padx=50, pady=50, command=myClick,\
    fg='blue', bg='red', bd = 5).grid(row=2,column=2)

# Entry widget
# width: width of the entry
# bg: the color of the entry
# fg: the color of letters written in the entry
# borderwidth: make the border being depth visually.
e = Entry(root, width=20, bg='blue', fg='white').grid()

# inserting icon to the top-left corner.
import os
from PIL import ImageTk, Image
gom_icon = os.getcwd()
gom_icon = gom_icon + "/gom.ico"
gom = ImageTk.PhotoImage(Image.open(gom_icon))
root.iconphoto(False, gom)


root.mainloop()