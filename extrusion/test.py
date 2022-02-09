from tkinter import *
w = Tk()
w.title("dd")
w.geometry("300x300")


def showSelected():
    a = lb.curselection()[0]
    print(a)
    itm = lb.get(a)
    var.set(itm)
var=StringVar()
lb=Listbox(w)
lb.pack()


lb.insert(0, "Iceland")
lb.insert(1, "USA")
lb.insert(2, "China")
lb.insert(3, "Europe")


disp = Label(w, textvariable=var)
disp.pack(pady=20)
Button(w, text="show selected", command = showSelected).pack()
w.mainloop()
