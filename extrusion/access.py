from tkinter import *

mlango = Tk()
mlango.title("Equipe")
mlango.geometry("250x400+800+300")
mlango.resizable(False, False)

def choice(group):
    mlango.destroy()
    global equipe
    equipe = (group)

btn1 = Button(mlango, text = "Equipe A", font=('calibre', 15, 'bold'),\
              height=2, width=8, bd=3, command = lambda: choice("A")).place(x=61, y=125)

btn2 = Button(mlango, text = "Equipe B", font=('calibre', 15, 'bold'),\
              height=2, width=8, bd=3, command = lambda: choice("B")).place(x=61, y=215)

btn3 = Button(mlango, text = "Equipe C", font=('calibre', 15, 'bold'),\
              height=2, width=8, bd=3, command = lambda: choice("C")).place(x=61, y=305)

mlango.mainloop()