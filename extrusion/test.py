a= "1"
b= 1.0
c = [a,b]
if int(a) == b:
    print('g')

print(str(b))
'''
from tkinter import *


class a:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x300")
        
        Button(self.master, text = 'click to open toplevel', command = self.open_top).pack()


    def open_top(self):
        newone(self)
        
def newone(self):
    self.top1 = Toplevel(self.master)
    self.top1.geometry('200x200')
    Button(self.top1, text = "click to open toplevel2", command = lambda: warn()).pack()
    self.top1.grab_set()

    def warn():
        a = Toplevel()
        a.geometry('100x100')
        Button(a, text="exit", command = a.destroy).pack()
        a.grab_set()


w = Tk()
a(w)


    
w.mainloop()
'''