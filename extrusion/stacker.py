from tkinter import *
from tkinter.font import BOLD
import tkinter.ttk as ttk
import sqlite3
from random import random


# create a window
window = Tk()
window.title("Stacker of Kim International")
window.geometry("1920x972")
window.resizable(0, 0)
# icon. memorize Gomsuni...
import os
from PIL import ImageTk, Image
gom_icon = os.getcwd()
gom_icon = gom_icon + "/gom.ico"
gom = ImageTk.PhotoImage(Image.open(gom_icon))
window.iconphoto(False, gom)

# create a menu bar
menu = Menu(window)

# menu1, file
def access():
    import login
    login.Access()
menu_file = Menu(menu, tearoff=0)
menu.add_cascade(label=" Fichier ", font=("Times New Roman", 15, "normal"), menu = menu_file)

menu_file.add_command(label = "   Access  ", font=("Times New Roman", 13, "normal"), command = access)
menu_file.add_command(label = "   Articles", font=("Times New Roman", 13, "normal"))
menu_file.add_separator()
menu_file.add_command(label = "   Quitter  ", font=("Times New Roman", 13, "normal"), command = window.destroy)

# menu2, view
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label=" Recherche ", font=("Times New Roman", 15, "normal"), menu = menu_view)
menu_view.add_command(label = "   Par article ", font=("Times New Roman", 13, "normal"), command=None)
menu_view.add_command(label = "   Par machine ", font=("Times New Roman", 13, "normal"), command=None)

# menu3, about
def message():
    from tkinter import messagebox
    messagebox.showinfo("information", "Si vous avez les questions pour ce logiciel, contactez celui qui a développé ce logiciel.\n Développeur: chu2540@nate.com")

menu_about = Menu(menu, tearoff=0)
menu.add_cascade(label=" A propos ", font=("Times New Roman", 15, "normal"), menu = menu_about)
menu_about.add_command(label = "   Information ",\
     font=("Times New Roman", 13, "normal"), command=message)

# Frame for treeview
frame_weight = Frame(window, width=1500).pack(side=RIGHT)

# style for column names
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview.Heading", font=('Calibre', 14, BOLD))

# style for the body of the treeview.
style.configure("mystyle.Treeview", rowheight=42, font=('calibre', 20))
style.map("Treeview", background=[('selected', 'blue')])

# TreeView
tree_weight = ttk.Treeview(frame_weight, height=22, style="mystyle.Treeview", selectmode='browse')
tree_weight['columns']=("ID", "Article", "Poid")
tree_weight.column('#0', width=0, stretch=NO)
tree_weight.column('ID', anchor=CENTER, width=70)
tree_weight.column('Article', anchor=CENTER, width=140)
tree_weight.column('Poid', anchor=CENTER, width=184)

tree_weight.heading('#0', text='', anchor=CENTER)
tree_weight.heading('ID', text='ID', anchor=CENTER)
tree_weight.heading('Article', text='Article', anchor=CENTER)
tree_weight.heading('Poid', text='Poid', anchor=CENTER)


# scollbar
scroll_y = Scrollbar(frame_weight, width=18, command=tree_weight.yview)
tree_weight.configure(yscroll = scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y, pady=4)

# to put the treeview, 'pack' function should be after all components of the treeview.
tree_weight.pack(padx=2, pady=2)

# bg.color of nodes of the treeview
# these settings should be placed before DB
tree_weight.tag_configure('odd', background="AntiqueWhite3")
tree_weight.tag_configure('even', background="azure")
        
# DB
rolls = []
for n in range(1,100):
    rolls.append((n, '05K/A', "{:.2f}" .format(13.5*(0.9+random()*0.2),2)))

for i in range(len(rolls)):
    if i % 2 == 0:
        tree_weight.insert('', END, values=rolls[i], tags = ('odd',))
    else:
        tree_weight.insert('', END, values=rolls[i], tags = ('even',))



# labels
article = StringVar()

label_date = Label(window, text="DATE",\
    font = ('Calibre', 20, BOLD)).place(x=460, y=120)
label_dot1 = Label(window, text=":",\
    font = ('Calibre', 20, BOLD)).place(x=640, y=120)

label_Equipe = Label(window, text="EQUIPE", \
    font = ('Calibre', 20, BOLD)).place(x=460, y=190)
label_dot2 = Label(window, text=":",\
    font = ('Calibre', 20, BOLD)).place(x=640, y=190)

label_machine = Label(window, text="MACHINE", \
    font = ('Calibre', 20, BOLD)).place(x=460, y=260)
label_dot3 = Label(window, text=":",\
    font = ('Calibre', 20, BOLD)).place(x=640, y=260)

label_production = Label(window, text="PRODUCTION", \
    font = ('Calibre', 20, BOLD)).place(x=460, y=330)
label_dot4 = Label(window, text=":",\
    font = ('Calibre', 20, BOLD)).place(x=640, y=330)

label_article = Label(window, text="ARTICLE", \
    font = ('Calibre', 20, BOLD)).place(x=460, y=400)
label_dot5 = Label(window, text=":",\
    font = ('Calibre', 20, BOLD)).place(x=640, y=400)

articles=["","05K/A", "05NK/G","08D", "08NK/G"]
combo_article = ttk.Combobox(window, width=10, textvariable=article,\
    values=articles,font = ('Calibre', 20, BOLD), state="readonly", justify="center")
combo_article.place(x=663, y=400)

label_poid = Label(window, text="POID", \
    font = ('Calibre', 20, BOLD)).place(x=460, y=470)
label_dot6 = Label(window, text=":",\
    font = ('Calibre', 20, BOLD)).place(x=640, y=470)
label_kg = Label(window, text="kg", \
    font = ('Calibre', 20, BOLD)).place(x=835, y=470)

# Entry
poid_var = StringVar()
ent_weight = Entry(window, font = ('Calibre', 20, BOLD), width=10, bd=3,\
    justify=RIGHT, textvariable=poid_var)
ent_weight.place(x=660, y=468)

# when choosing a thing of treeview
def selecting(event):
    for info in tree_weight.selection():
        items = tree_weight.item(info)

        ent_weight.delete(0, END)
        ent_weight.insert(0, items['values'][2])
        combo_article.set(items['values'][1])

tree_weight.bind('<<TreeviewSelect>>', selecting)


# variable labels
def click_machines():
    from datetime import datetime, timedelta
    frame_labels = Frame(window, width=800, bg='black').pack(side=LEFT)

# imports for a DB
#import os
#from datetime import datetime
# getting the path
#path = os.getcwd()
#path = path + "/DB/rolls/rolls.db"
# create a connection
#conn = sqlite3.connect(path)
# create a cursor
#c = conn.cursor()
# create a table
#c.execute("""CREATE TABLE rolls (
#    RealTime datetime,
#    Date text,
#    Article text,
#    Weight float,
#    Machine text,
#    product code integer,
#    worker ID integer
#    modified interger
#    )""")

#conn.commit()


# buttons for machines
# grid information for buttons
# x-axis, 1000, 1090, 1180, 1270, 1360, 1450, 1540, 1630, 1720, 1810
# y-axis, 20, 100, 180, 260, 400, 480, 560, 640, 780, 860

A1 = Button(window, text = "A1", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1000, y=20)
A2 = Button(window, text = "A2", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1090, y=20)
A3 = Button(window, text = "A3", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1180, y=20)
A4 = Button(window, text = "A4", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1270, y=20)
B1 = Button(window, text = "B1", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1360, y=20)
B2 = Button(window, text = "B2", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1450, y=20)
B3 = Button(window, text = "B3", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1540, y=20)
B4 = Button(window, text = "B4", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1630, y=20)
C1 = Button(window, text = "C1", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1720, y=20)
C2 = Button(window, text = "C2", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1810, y=20)
D1 = Button(window, text = "D1", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1720, y=100)
D2 = Button(window, text = "D2", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1540, y=100)
E1 = Button(window, text = "E1", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1360, y=100)
E2 = Button(window, text = "E2", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1270, y=100)
E3 = Button(window, text = "E3", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1090, y=100)
F1 = Button(window, text = "F1", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1540, y=260)
F2 = Button(window, text = "F2", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1360, y=260)
F3 = Button(window, text = "F3", font=('Times New Roman', 17, 'bold'), bg="goldenrod1",\
              height=2, width=3, bd=3, command = None).place(x=1360, y=180)
G1 = Button(window, text = "G1", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1000, y=640)
G2 = Button(window, text = "G2", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1000, y=560)
G3 = Button(window, text = "G3", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1000, y=480)
H1 = Button(window, text = "H1", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1000, y=400)
H2 = Button(window, text = "H2", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1180, y=400)
H3 = Button(window, text = "H3", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1270, y=400)
I1 = Button(window, text = "I1", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1360, y=400)
I2 = Button(window, text = "I2", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1450, y=400)
I3 = Button(window, text = "I3", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1540, y=400)
J1 = Button(window, text = "J1", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1540, y=640)
J2 = Button(window, text = "J2", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1450, y=640)
J3 = Button(window, text = "J3", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1360, y=640)
J4 = Button(window, text = "J4", font=('Times New Roman', 17, 'bold'), bg="tomato",\
              height=2, width=3, bd=3, command = None).place(x=1270, y=640)
K1 = Button(window, text = "K1", font=('Times New Roman', 17, 'bold'), bg="light sea green",\
              height=2, width=3, bd=3, command = None).place(x=1000, y=780)
K2 = Button(window, text = "K2", font=('Times New Roman', 17, 'bold'), bg="light sea green",\
              height=2, width=3, bd=3, command = None).place(x=1090, y=780)
K3 = Button(window, text = "K3", font=('Times New Roman', 17, 'bold'), bg="light sea green",\
              height=2, width=3, bd=3, command = None).place(x=1180, y=780)
K4 = Button(window, text = "K4", font=('Times New Roman', 17, 'bold'), bg="light sea green",\
              height=2, width=3, bd=3, command = None).place(x=1270, y=780)
L1 = Button(window, text = "L1", font=('Times New Roman', 17, 'bold'), bg="MediumPurple1",\
              height=2, width=3, bd=3, command = None).place(x=1540, y=860)
L2 = Button(window, text = "L2", font=('Times New Roman', 17, 'bold'), bg="MediumPurple1",\
              height=2, width=3, bd=3, command = None).place(x=1630, y=860)
L3 = Button(window, text = "L3", font=('Times New Roman', 17, 'bold'), bg="MediumPurple1",\
              height=2, width=3, bd=3, command = None).place(x=1720, y=860)
L4 = Button(window, text = "L4", font=('Times New Roman', 17, 'bold'), bg="MediumPurple1",\
              height=2, width=3, bd=3, command = None).place(x=1720, y=780)
M1 = Button(window, text = "M1", font=('Times New Roman', 17, 'bold'), bg="light sea green",\
              height=2, width=3, bd=3, command = None).place(x=1000, y=860)
M2 = Button(window, text = "M2", font=('Times New Roman', 17, 'bold'), bg="light sea green",\
              height=2, width=3, bd=3, command = None).place(x=1090, y=860)
PP1 = Button(window, text = "PP1", font=('Times New Roman', 17, 'bold'), bg="light sea green",\
              height=2, width=3, bd=3, command = None).place(x=1180, y=860)
PP2 = Button(window, text = "PP2", font=('Times New Roman', 17, 'bold'), bg="light sea green",\
              height=2, width=3, bd=3, command = None).place(x=1270, y=860)

  


window.config(menu=menu)
window.mainloop()