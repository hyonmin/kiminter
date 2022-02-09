from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('checkboxes')
root.geometry("400x400")

# test checkbox1, a checkbox checked gives a integer value
w = LabelFrame(root, text="checkbox1")
w.grid(row=0,column=0)

def show():
    lb = Label(w, text=var.get()).pack()

var = IntVar()

c1=Checkbutton(w, text = 'PIZZA', variable=var)
c1.pack()

btn1 = Button(w, text="print", command= show).pack()



# test checkbox2, a checkbox checked gives a string value
x = LabelFrame(root, text="checkbox2")
x.grid(row=0,column=1)

def show():
    lbx = Label(x, text=svar.get()).pack()

svar = StringVar()

c2=Checkbutton(x, text = 'PIZZA', variable=svar, onvalue="PIZZA", offvalue="NO PIZZA!?")
# choose 'deselect' or 'select'
#c2.deselect()
c2.select()
c2.pack()

btn2 = Button(x, text="print", command= show).pack()

y = LabelFrame(root, text="checkbox3")
y.grid(row=1, column=0, padx=50, pady=50)
#style1
Checkbutton(y, text="option1", font= 'BahnschriftLight 13').pack()

root.mainloop()