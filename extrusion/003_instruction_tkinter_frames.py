from tkinter import *

root = Tk()
root.title("Learning Frames")

frame = LabelFrame(root, text = 'this is my frame...', padx=50, pady=50)
frame.grid(row= 1, column =1, padx=100, pady=100)

b = Button(frame, text = "Don't click here!")
b.pack()

b2 = Button(root, text = "or here")
b2.grid(row=0, column=0)


# a frame for radiobuttons
frame2 = LabelFrame(root,text="radio buttons", padx=50, pady=50)
frame2.grid(row=2,column=0, columnspan=2)

# IntVar let 'r' a integer variable as an option in radiobutton.
r = IntVar()

# settting, the variable 'r' equals '2' which is already assigned with value=2 in the radiobutton option
# interesting, string '2' is connected the value integer '2' in the option of radiobutton.
r.set("2")

def clicked(value):
    radio_Label = Label(frame2, text = value)
    radio_Label.pack()


Radiobutton(frame2, text='Option 1', variable=r, value=1, command= lambda: clicked(r.get())).pack()
Radiobutton(frame2, text='Option 2', variable=r, value=2, command= lambda: clicked(r.get())).pack()
Radiobutton(frame2, text='Option 3', variable=r, value=3, command= lambda: clicked(r.get())).pack()
Radiobutton(frame2, text='Option 4', variable=r, value=4, command= lambda: clicked(r.get())).pack()
Radiobutton(frame2, text='Option 5', variable=r, value=5, command= lambda: clicked(r.get())).pack()

radio_Label = Label(frame2, text=r.get()).pack()

bt = Button(frame2, text = 'click me!', command = lambda: clicked(r.get())).pack()



# another example of radiobuttons

frame_pizza = LabelFrame(root, text = 'pizza', padx =50, pady=50)
frame_pizza.grid(row=3, column=0, columnspan=2)

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("cheese", "cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

# let pizza a string variable
pizza = StringVar()
pizza.set("Pepperoni")

def pizza_click(value):
    pizza_label = Label(frame_pizza, text=value).pack()

for text, mode in MODES:
    Radiobutton(frame_pizza, text = text, variable = pizza, value=mode).pack(anchor=E)

btn = Button(frame_pizza, text = 'click me!', command = lambda: pizza_click(pizza.get())).pack()

root.mainloop()