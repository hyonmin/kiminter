from calendar import Calendar
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import tkinter.ttk as ttk
from tkcalendar import Calendar
from random import random
from datetime import datetime, timedelta
from PIL import ImageTk, Image
import os
#----------------------font-----------------------------
# Labeltitle
f1 = ('times new roman', 50, 'bold')
#Labelframes
f2 = ('arial', 20, 'bold')
#calendar
f3 = ('arial', 18, 'bold')
#menu1
f4 = ('arial', 15, 'normal')
#menu2
f5 = ('arial', 14, 'normal')
#buttons
f6 = ('times new roman', 17, 'bold')

def main():
    root = Tk()
    app = window1(root)
    root.mainloop()

# to memorize gomsuni...
def icon(self):
    gom_icon = os.getcwd()
    gom_icon = gom_icon + "/gom.ico"
    gom = ImageTk.PhotoImage(Image.open(gom_icon))
    self.iconphoto(False, gom)

class window1:
    def __init__(self, master):
        self.master = master
        self.master.title("System Login")
        self.master.geometry('1000x720+455+100')
        self.master.resizable(False, False)
        # for icon
        icon(self.master)
        
        self.frame = Frame(self.master, bg='dodger blue', padx=50, pady=20)
        self.frame.grid(row=0,column=0)
#----------------------frames---------------------------
        self.LabelTitle = Label(self.frame, text = 'Kim International Stacker - E',\
            bg='dodger blue', foreground='white', font=f1, bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.Loginframe1 = LabelFrame(self.frame, text = " Calendrier ", bg='dodger blue',\
            width=500, height=300, bd=5, relief='ridge', font=f2, padx=30, pady=35)
        self.Loginframe1.grid(row=1, column=0, rowspan=2, padx=10, pady=25)
        
        self.Loginframe2 = LabelFrame(self.frame, text = " Jour / Soir ", bg='dodger blue',\
            width=500, height=100, bd=5, relief='ridge', font=f2)
        self.Loginframe2.grid(row=1, column=1, pady=0)
        
        self.Loginframe3 = LabelFrame(self.frame, text = " Equipe ", bg='dodger blue',\
            width=500, height=200, bd=5, relief='ridge', font=f2)
        self.Loginframe3.grid(row=2, column=1)
#------------------------calendar on frame1-----------------------------
        self.d = datetime.today().strftime('%d')
        self.m = datetime.today().strftime('%m')
        self.y = datetime.today().strftime('%Y')
        # initial date
        self.init=datetime(2022,1,1)
        # min date
        self.min= datetime.today()- timedelta(days=1)
        # max date
        self.max= datetime.today()
        # create a calendar
        self.cal = Calendar(self.Loginframe1, locale="fr_be", selectmode='day',font=f3,\
            firstweekday="sunday", year=int(self.y), month=int(self.m), day=int(self.d),\
            mindate=self.min, maxdate=self.max, date_pattern="dd/mm/yyyy")
        self.cal.grid(row=1, column=0)

        #print the date, when selected
        self.cal.bind("<<CalendarSelected>>",lambda event: self.decision_EQ())

        #print the initially selected date == today
        self.calSelected = Label(self.Loginframe1, text=self.cal.get_date(),\
            bg="dodger blue", font=f3)
        self.calSelected.grid(row=0,column=0)
#--------------------date on master-------------------------------------
        Label(self.master, text=self.cal.get_date()).grid(row=1,column=0)
#-------------------------day and night decision buttons----------------
        self.js =IntVar()
        self.j = Checkbutton(self.Loginframe2, text = "Jour", variable=self.js,\
            highlightthickness=0,relief='flat', overrelief='flat',\
            bg="dodger blue", fg='white', font=f2, onvalue=0, command = self.decision_EQ,\
            selectcolor="dodger blue", activebackground='dodger blue')
        self.j.grid(row=0, column=0, padx=30, pady=20)

        self.s = Checkbutton(self.Loginframe2, text = "Soir", variable=self.js,\
            highlightthickness=0, relief='flat', overrelief='flat',\
            bg="dodger blue", fg='white', font=f2, onvalue=1, command = self.decision_EQ,\
            selectcolor="dodger blue", activebackground='dodger blue')
        self.s.grid(row=0, column=1, padx=45)
#---------------------------------buttons of equipes----------------------------

        self.EQA = Button(self.Loginframe3, text="Equipe A", font=f2, padx=30, command=self.login_system)
        self.EQA.grid(row=0, column=0, padx=85, pady=20)

        self.EQB = Button(self.Loginframe3, text="Equipe B", font=f2, padx=30, command=self.login_system)
        self.EQB.grid(row=1, column=0)

        self.EQC = Button(self.Loginframe3, text="Equipe C", font=f2, padx=30, command=self.login_system)
        self.EQC.grid(row=2, column=0, pady=20)

        # according to the date of today, the statements of buttons are changed
        self.decision_EQ()
#-------------------------------------------------------------

    def decision_EQ(self):
        self.calSelected = Label(self.Loginframe1, text=self.cal.get_date(),\
        bg="dodger blue", font=f3)
        self.calSelected.grid(row=0, column=0)
        self.dt=self.cal.get_date()[0:2]
        self.mt=self.cal.get_date()[3:5]
        self.yt=self.cal.get_date()[6:10]
        self.today=datetime(int(self.yt), int(self.mt), int(self.dt))
        self.ddiff= self.today-self.init
    
        if self.ddiff.days % 3 == 0:
            self.EQA.configure(state=DISABLED)
            self.EQB.configure(state=NORMAL)
            self.EQC.configure(state=NORMAL)
            if self.js.get() == 0:
                self.EQC.configure(state=DISABLED)
            else:
                self.EQB.configure(state=DISABLED)

        elif self.ddiff.days % 3 == 1:
            self.EQA.configure(state=NORMAL)
            self.EQB.configure(state=NORMAL)
            self.EQC.configure(state=DISABLED)
            if self.js.get() == 0:
                self.EQB.configure(state=DISABLED)
            else:
                self.EQA.configure(state=DISABLED)
        else:
            self.EQA.configure(state=NORMAL)
            self.EQB.configure(state=DISABLED)
            self.EQC.configure(state=NORMAL)
            if self.js.get() == 0:
                self.EQA.configure(state=DISABLED)
            else:
                self.EQC.configure(state=DISABLED)
#-------------------------------login--------------------------------
    def login_system(self):
        #self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = window2(self.newWindow)

class window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Extrusion Stacker")
        self.master.geometry('1920x972')
        self.master.resizable(0, 0)
        icon(self.master)
        
        #def access():
            #return
        
        self.menu = Menu(self.master)
        # menu1, file
        self.menu_file = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=" Fichier ", font=("Times New Roman", 15, "normal"), menu = self.menu_file)

        self.menu_file.add_command(label = "   Access  ", font=("Times New Roman", 13, "normal"), command = None)
        self.menu_file.add_command(label = "   Articles", font=("Times New Roman", 13, "normal"))
        self.menu_file.add_separator()
        self.menu_file.add_command(label = "   Quitter  ", font=("Times New Roman", 13, "normal"), command = self.master.destroy)

        # menu2, view
        self.menu_view = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=" Recherche ", font=("Times New Roman", 15, "normal"), menu = self.menu_view)
        self.menu_view.add_command(label = "   Par article ", font=("Times New Roman", 13, "normal"), command=None)
        self.menu_view.add_command(label = "   Par machine ", font=("Times New Roman", 13, "normal"), command=None)

        # menu3, about
        def message():
            from tkinter import messagebox
            messagebox.showinfo("information", "Si vous avez les questions pour ce logiciel, contactez celui qui a développé ce logiciel.\n Développeur: chu2540@nate.com")

        self.menu_about = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=" A propos ", font=("Times New Roman", 15, "normal"), menu = self.menu_about)
        self.menu_about.add_command(label = "   Information ",\
             font=("Times New Roman", 13, "normal"), command=message)

        self.master.config(menu=self.menu)
#=======================================================================frames=======================================
        #Frame for a treeview
        self.frame_weight = LabelFrame(self.master, text=" List", font=f2, relief="flat")
        self.frame_weight.pack(side="left", padx=(15,0), pady=15)

        #Frame for buttons
        self.frame_buttons = LabelFrame(self.master, text="  Machines  ", font=f2, padx=20, pady=40)
        self.frame_buttons.pack(side='right', padx=(0,30))

        #Frame for labels
        self.frame_labels = LabelFrame(self.master, text="  Informations  ", font=f2, padx=20, pady=40)
        self.frame_labels.pack(side='right', padx=(0,30))

#=====================================================================buttons for machines==========================
        # buttons for machines
        # grid information for buttons
        # x-axis, 1000, 1090, 1180, 1270, 1360, 1450, 1540, 1630, 1720, 1810
        # y-axis, 20, 100, 180, 260, 400, 480, 560, 640, 780, 860

        self.A1 = Button(self.frame_buttons, text = "A1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.A1.grid(padx=0,  pady=0, row=0, column=0)

        self.A2 = Button(self.frame_buttons, text = "A2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.A2.grid(padx=25,  pady=0, row=0, column=1)

        self.A3 = Button(self.frame_buttons, text = "A3", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.A3.grid(padx=0,  pady=0, row=0, column=2)

        self.A4 = Button(self.frame_buttons, text = "A4", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.A4.grid(padx=25,  pady=0, row=0, column=3)

        self.B1 = Button(self.frame_buttons, text = "B1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.B1.grid(padx=0,  pady=0, row=0, column=4)

        self.B2 = Button(self.frame_buttons, text = "B2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.B2.grid(padx=25,  pady=0, row=0, column=5)

        self.B3 = Button(self.frame_buttons, text = "B3", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.B3.grid(padx=0,  pady=0, row=0, column=6)

        self.B4 = Button(self.frame_buttons, text = "B4", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.B4.grid(padx=(25,0),  pady=0, row=0, column=7)

        self.C1 = Button(self.frame_buttons, text = "C1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.C1.grid(padx=0,  pady=25, row=1, column=0)

        self.C2 = Button(self.frame_buttons, text = "C2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.C2.grid(padx=0,  pady=0, row=1, column=1)

        self.D1 = Button(self.frame_buttons, text = "D1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.D1.grid(padx=0,  pady=0, row=1, column=2)

        self.D2 = Button(self.frame_buttons, text = "D2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.D2.grid(padx=0,  pady=0, row=1, column=3)

        self.E1 = Button(self.frame_buttons, text = "E1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.E1.grid(padx=0,  pady=0, row=1, column=4)

        self.E2 = Button(self.frame_buttons, text = "E2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.E2.grid(padx=0,  pady=0, row=1, column=5)

        self.E3 = Button(self.frame_buttons, text = "E3", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.E3.grid(padx=0,  pady=0, row=1, column=6)

        self.F1 = Button(self.frame_buttons, text = "F1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.F1.grid(padx=(25,0),  pady=0, row=1, column=7)

        self.F2 = Button(self.frame_buttons, text = "F2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.F2.grid(padx=0,  pady=0, row=2, column=0)

        self.F3 = Button(self.frame_buttons, text = "F3", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = None)
        self.F3.grid(padx=0,  pady=0, row=2, column=1)

        self.G1 = Button(self.frame_buttons, text = "G1", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.G1.grid(padx=0,  pady=(55,25), row=3, column=0)

        self.G2 = Button(self.frame_buttons, text = "G2", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.G2.grid(padx=0,  pady=(55,25), row=3, column=1)

        self.G3 = Button(self.frame_buttons, text = "G3", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.G3.grid(padx=0,  pady=(55,25), row=3, column=2)

        self.H1 = Button(self.frame_buttons, text = "H1", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.H1.grid(padx=0,  pady=(55,25), row=3, column=3)

        self.H2 = Button(self.frame_buttons, text = "H2", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.H2.grid(padx=0,  pady=(55,25), row=3, column=4)

        self.H3 = Button(self.frame_buttons, text = "H3", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.H3.grid(padx=0,  pady=(55,25), row=3, column=5)

        self.I1 = Button(self.frame_buttons, text = "I1", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.I1.grid(padx=0,  pady=(55,25), row=3, column=6)

        self.I2 = Button(self.frame_buttons, text = "I2", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.I2.grid(padx=(25,0),  pady=(55,25), row=3, column=7)

        self.I3 = Button(self.frame_buttons, text = "I3", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.I3.grid(padx=0,  pady=0, row=4, column=0)

        self.J1 = Button(self.frame_buttons, text = "J1", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.J1.grid(padx=0,  pady=0, row=4, column=1)

        self.J2 = Button(self.frame_buttons, text = "J2", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.J2.grid(padx=0,  pady=0, row=4, column=2)

        self.J3 = Button(self.frame_buttons, text = "J3", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.J3.grid(padx=0,  pady=0, row=4, column=3)

        self.J4 = Button(self.frame_buttons, text = "J4", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = None)
        self.J4.grid(padx=0,  pady=0, row=4, column=4)

        self.K1 = Button(self.frame_buttons, text = "K1", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = None)
        self.K1.grid(padx=0,  pady=(55,25), row=5, column=0)

        self.K2 = Button(self.frame_buttons, text = "K2", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = None)
        self.K2.grid(padx=0,  pady=(55,25), row=5, column=1)

        self.K3 = Button(self.frame_buttons, text = "K3", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = None)
        self.K3.grid(padx=0,  pady=(55,25), row=5, column=2)

        self.K4 = Button(self.frame_buttons, text = "K4", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = None)
        self.K4.grid(padx=0,  pady=(55,25), row=5, column=3)

        self.L1 = Button(self.frame_buttons, text = "L1", font=f6, bg="MediumPurple1",\
                    height=2, width=3, bd=3, command = None)
        self.L1.grid(padx=0,  pady=(55,25), row=5, column=4)

        self.L2 = Button(self.frame_buttons, text = "L2", font=f6, bg="MediumPurple1",\
                    height=2, width=3, bd=3, command = None)
        self.L2.grid(padx=0,  pady=(55,25), row=5, column=5)

        self.L3 = Button(self.frame_buttons, text = "L3", font=f6, bg="MediumPurple1",\
                    height=2, width=3, bd=3, command = None)
        self.L3.grid(padx=0,  pady=(55,25), row=5, column=6)

        self.L4 = Button(self.frame_buttons, text = "L4", font=f6, bg="MediumPurple1",\
                    height=2, width=3, bd=3, command = None)
        self.L4.grid(padx=(25,0),  pady=(55,25), row=5, column=7)

        self.M1 = Button(self.frame_buttons, text = "M1", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = None)
        self.M1.grid(padx=0,  pady=0, row=6, column=0)

        self.M2 = Button(self.frame_buttons, text = "M2", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = None)
        self.M2.grid(padx=0,  pady=0, row=6, column=1)

        self.PP1 = Button(self.frame_buttons, text = "PP1", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = None)
        self.PP1.grid(padx=0,  pady=(55,0), row=7, column=0)

        self.PP2 = Button(self.frame_buttons, text = "PP2", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = None)
        self.PP2.grid(padx=0,  pady=(55,0), row=7, column=1)

#====================================================treeview================================================
        # style for column names
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview.Heading", font=f4)
        # style for the body of the treeview.
        self.style.configure("mystyle.Treeview", rowheight=42, font=f6)
        self.style.map("Treeview", background=[('selected', 'blue')])

        # TreeView
        self.tree_weight = ttk.Treeview(self.frame_weight, height=22, style="mystyle.Treeview", selectmode='browse')
        self.tree_weight['columns']=("ID", "Article", "Poid")
        self.tree_weight.column('#0', width=0, stretch=NO)
        self.tree_weight.column('ID', anchor=CENTER, width=70)
        self.tree_weight.column('Article', anchor=CENTER, width=140)
        self.tree_weight.column('Poid', anchor=CENTER, width=184)

        self.tree_weight.heading('#0', text='', anchor=CENTER)
        self.tree_weight.heading('ID', text='ID', anchor=CENTER)
        self.tree_weight.heading('Article', text='Article', anchor=CENTER)
        self.tree_weight.heading('Poid', text='Poid', anchor=CENTER)

        # scollbar
        self.scroll_y = Scrollbar(self.frame_weight, width=18, command=self.tree_weight.yview)
        self.tree_weight.configure(yscroll = self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y, pady=4)
        
        # bg.color of nodes of the treeview
        # these settings should be placed before DB
        self.tree_weight.tag_configure('odd', background="AntiqueWhite3")
        self.tree_weight.tag_configure('even', background="azure")

        # to put the treeview, 'pack' function should be after all components of the treeview.
        self.tree_weight.pack(padx=2, pady=2)

        
        for n in range(1,100):
            if n % 2 == 0:
                self.tree_weight.insert('', 'end', values=(n, '05K/A', "{:.2f}" .format(13.5*(0.9+random()*0.2),2)), tags = ('odd',))
            else:
                self.tree_weight.insert('', 'end', values=(n, '05K/A', "{:.2f}" .format(13.5*(0.9+random()*0.2),2)), tags = ('even',))
       
'''        
        # DB
        rolls = []
        for a in range(1,100):
            self.tree_weight.insert('', 'end', values=(a, '05K/A', "{:.2f}" .format(13.5*(0.9+random()*0.2),2)), tags = ('even',))
            rolls.append(a, '05K/A', "{:.2f}" .format(13.5*(0.9+random()*0.2),2))

        for i in range(len(rolls)):
            if i % 2 == 0:
                self.tree_weight.insert('', 'end', values=rolls[i], tags = ('odd',))
            else:
                self.tree_weight.insert('', 'end', values=rolls[i], tags = ('even',))
'''

'''
        # labels
        self.article = StringVar()

        self.label_date = Label(self.master, text="DATE",\
            font = f2).place(x=460, y=120)
        self.label_dot1 = Label(self.master, text=":",\
            font = f2).place(x=640, y=120)

        self.label_Equipe = Label(self.master, text="EQUIPE", \
            font = f2).place(x=460, y=190)
        self.label_dot2 = Label(self.master, text=":",\
            font = f2).place(x=640, y=190)

        self.label_machine = Label(self.master, text="MACHINE", \
            font = f2).place(x=460, y=260)
        self.label_dot3 = Label(self.master, text=":",\
            font = f2).place(x=640, y=260)

        self.label_production = Label(self.master, text="PRODUCTION", \
            font = f2).place(x=460, y=330)
        self.label_dot4 = Label(self.master, text=":",\
            font = f2).place(x=640, y=330)

        self.label_article = Label(self.master, text="ARTICLE", \
            font = f2).place(x=460, y=400)
        self.label_dot5 = Label(self.master, text=":",\
            font = f2).place(x=640, y=400)

        articles=["","05K/A", "05NK/G","08D", "08NK/G"]
        self.combo_article = ttk.Combobox(self.master, width=10, textvariable=self.article,\
            values=articles,font = f2, state="readonly", justify="center")
        self.combo_article.place(x=663, y=400)

        self.label_poid = Label(self.master, text="POID", \
            font = f2).place(x=460, y=470)
        self.label_dot6 = Label(self.master, text=":",\
            font = f2).place(x=640, y=470)
        self.label_kg = Label(self.master, text="kg", \
            font = f2).place(x=835, y=470)

        # Entry
        self.poid_var = StringVar()
        self.ent_weight = Entry(self.master, font = f2, width=10, bd=3,\
            justify=RIGHT, textvariable=self.poid_var)
        self.ent_weight.place(x=660, y=468)

        # when choosing a thing of treeview
        def selecting(event):
            for info in self.tree_weight.selection():
                items = self.tree_weight.item(info)

                self.ent_weight.delete(0, END)
                self.ent_weight.insert(0, items['values'][2])
                self.combo_article.set(items['values'][1])

        self.tree_weight.bind('<<TreeviewSelect>>', selecting)


        # variable labels
        def click_machines():
            from datetime import datetime, timedelta
            self.frame_labels = Frame(self.master, width=800, bg='black').pack(side=LEFT)
'''
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
        
        #self.master.mainloop()

class window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.master.mainloop()


if __name__ == '__main__':
    main()