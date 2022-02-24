from calendar import Calendar
#from email.policy import default
from tkinter import *
#import tkinter.messagebox
from tkinter import ttk
import tkinter.ttk as ttk
#from numpy import var
from tkcalendar import Calendar
from random import random
from datetime import datetime, timedelta
from PIL import ImageTk, Image
import os
#----------------------font-----------------------------
# Labeltitle
f1 = ('Times New Roman', 50, 'bold')
#Labelframes
f2 = ('arial', 20, 'bold')
#calendar
f3 = ('arial', 18, 'bold')
# treeview
f4 = ('arial', 15, 'normal')
#menu2
f5 = ('Times New Roman', 13, 'normal')
#buttons
f6 = ('Times New Roman', 17, 'bold')
#menu1
f7 = ('Times New Roman', 15, 'normal')


# keys; 'date'(for diaplay the date)
# keys; 'logintime(login time)
# keys; 'equipe'(the name of group)
# keys; 'name'(access name)
# keys; 'jour/soir'(0: jour, 1:soir)

default_data={}
months = ('janv', 'févr', 'mars', 'avril', 'mai', 'juin', 'juil', 'août', 'sept', 'oct', 'nov', 'déc')

def main():
    root = Tk()
    window1(root)
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

        self.EQA = Button(self.Loginframe3, text="A", font=f2, padx=30, pady=10,\
            command=self.login_system)
        self.EQA.grid(row=1, column=0, padx=15)

        self.EQB = Button(self.Loginframe3, text="B", font=f2, padx=30, pady=10,\
            command=self.login_system)
        self.EQB.grid(row=1, column=1, padx=15, pady=25)

        self.EQC = Button(self.Loginframe3, text="C", font=f2, padx=30, pady=10,\
            command=self.login_system)
        self.EQC.grid(row=1, column=2, padx=15)
        
        self.lblnom = Label(self.Loginframe3, text="Nom", font=f2, bg='dodger blue')
        self.lblnom.grid(row=0, column=0, pady=35)
        self.Nom = Entry(self.Loginframe3, font=f2, width=13)
        self.Nom.grid(row=0, column=1, columnspan=2)

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
        default_data['date'] = "le" + self.today.strftime("%d")\
            +", "+ months[int(self.mt)-1] + ". " + self.today.strftime("%Y")
        default_data['logintime'] = datetime.today()

        if self.ddiff.days % 3 == 0:
            self.EQA.configure(state='disabled')
            self.EQB.configure(state='normal')
            self.EQC.configure(state='normal')
            if self.js.get() == 0:
                self.EQC.configure(state='disabled')
                default_data['equipe'] = "B"
                default_data['jour/soir'] = self.js.get()
            else:
                self.EQB.configure(state='disabled')
                default_data['equipe'] = "C"
                default_data['jour/soir'] = self.js.get()

        elif self.ddiff.days % 3 == 1:
            self.EQA.configure(state='normal')
            self.EQB.configure(state='normal')
            self.EQC.configure(state='disabled')
            if self.js.get() == 0:
                self.EQB.configure(state='disabled')
                default_data['equipe'] = "A"
                default_data['jour/soir'] = self.js.get()
            else:
                self.EQA.configure(state='disabled')
                default_data['equipe'] = "B"
                default_data['jour/soir'] = self.js.get()
        else:
            self.EQA.configure(state='normal')
            self.EQB.configure(state='disabled')
            self.EQC.configure(state='normal')
            if self.js.get() == 0:
                self.EQA.configure(state='disabled')
                default_data['equipe'] = "C"
                default_data['jour/soir'] = self.js.get()
            else:
                self.EQC.configure(state='disabled')
                default_data['equipe'] = "A"
                default_data['jour/soir'] = self.js.get()
#-------------------------------login--------------------------------
    def login_system(self):
        if self.Nom.get().strip() =="":
            return
        else:
            default_data['name'] = self.Nom.get().strip()
            self.master.destroy()
            root = Tk()
            window2(root)
        

class window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Extrusion Stacker")
        self.master.geometry('1920x972')
        self.master.resizable(0, 0)
        icon(self.master)
        
        self.menu = Menu(self.master)
        # menu1, file
        self.menu_file = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=" Fichier ", font=f7, menu = self.menu_file)

        self.menu_file.add_command(label = "   Access  ", font=f5, command = self.access)
        self.menu_file.add_command(label = "   Articles", font=f5, command = self.setting_articles)
        self.menu_file.add_separator()
        self.menu_file.add_command(label = "   Quitter  ", font=f5, command = self.master.destroy)

        # menu2, view
        self.menu_view = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=" Recherche ", font=f7, menu = self.menu_view)
        self.menu_view.add_command(label = "   Par article ", font=f5, command=None)
        self.menu_view.add_command(label = "   Par machine ", font=f5, command=None)

        # menu3, about
        def message():
            from tkinter import messagebox
            messagebox.showinfo("information", "Si vous avez les questions pour ce logiciel, contactez celui qui a développé ce logiciel.\n Développeur: chu2540@nate.com")

        self.menu_about = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=" A propos ", font=f7, menu = self.menu_about)
        self.menu_about.add_command(label = "   Information ",\
             font=f5, command=message)

        self.master.config(menu=self.menu)
#=======================================================================frames=======================================
        #Frame for a treeview
        self.frame_weight = LabelFrame(self.master, text=" List", font=f2, relief="flat")
        self.frame_weight.pack(side="left", padx=(15,0), pady=15)

        #Frame for buttons
        self.frame_buttons = LabelFrame(self.master, text="  Machines  ", font=f2, padx=20, pady=40)
        self.frame_buttons.pack(side='right', padx=(0,30))

        #Frame for labels
        self.frame_labels = LabelFrame(self.master, text="Informations", font=f2, padx=20, pady=40, relief="flat")
        self.frame_labels.pack(side='top', padx=(80,0), pady=15, fill="x")

#=====================================================================buttons for machines==========================
        # buttons for machines
        # grid information for buttons
        self.list_btns = {}
        self.color1= ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'D1',\
            'D2', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']
        self.color2 = ['G1', 'G2', 'G3', 'H1', 'H2','H3', 'I1', 'I2', 'I3', 'J1', 'J2', 'J3','J4']
        self.color3 = ['K1', 'K2', 'K3', 'K4', 'M1', 'M2', 'PP1', 'PP2']
        self.color4 = ['L1', 'L2', 'L3', 'L4']
    
        self.A1 = Button(self.frame_buttons, text = "A1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("A1"))
        self.A1.grid(padx=0,  pady=0, row=0, column=0)
        self.list_btns["A1"]= self.A1

        self.A2 = Button(self.frame_buttons, text = "A2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("A2"))
        self.A2.grid(padx=25,  pady=0, row=0, column=1)
        self.list_btns["A2"]= self.A2

        self.A3 = Button(self.frame_buttons, text = "A3", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("A3"))
        self.A3.grid(padx=0,  pady=0, row=0, column=2)
        self.list_btns["A3"]= self.A3

        self.A4 = Button(self.frame_buttons, text = "A4", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("A4"))
        self.A4.grid(padx=25,  pady=0, row=0, column=3)
        self.list_btns["A4"]= self.A4

        self.B1 = Button(self.frame_buttons, text = "B1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("B1"))
        self.B1.grid(padx=0,  pady=0, row=0, column=4)
        self.list_btns["B1"]= self.B1

        self.B2 = Button(self.frame_buttons, text = "B2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("B2"))
        self.B2.grid(padx=25,  pady=0, row=0, column=5)
        self.list_btns["B2"]= self.B2

        self.B3 = Button(self.frame_buttons, text = "B3", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("B3"))
        self.B3.grid(padx=0,  pady=0, row=0, column=6)
        self.list_btns["B3"]= self.B3

        self.B4 = Button(self.frame_buttons, text = "B4", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("B4"))
        self.B4.grid(padx=(25,0),  pady=0, row=0, column=7)
        self.list_btns["B4"]= self.B4

        self.C1 = Button(self.frame_buttons, text = "C1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("C1"))
        self.C1.grid(padx=0,  pady=25, row=1, column=0)
        self.list_btns["C1"]= self.C1

        self.C2 = Button(self.frame_buttons, text = "C2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("C2"))
        self.C2.grid(padx=0,  pady=0, row=1, column=1)
        self.list_btns["C2"]= self.C2

        self.D1 = Button(self.frame_buttons, text = "D1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("D1"))
        self.D1.grid(padx=0,  pady=0, row=1, column=2)
        self.list_btns["D1"]= self.D1

        self.D2 = Button(self.frame_buttons, text = "D2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("D2"))
        self.D2.grid(padx=0,  pady=0, row=1, column=3)
        self.list_btns["D2"]= self.D2

        self.E1 = Button(self.frame_buttons, text = "E1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("E1"))
        self.E1.grid(padx=0,  pady=0, row=1, column=4)
        self.list_btns["E1"]= self.E1

        self.E2 = Button(self.frame_buttons, text = "E2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("E2"))
        self.E2.grid(padx=0,  pady=0, row=1, column=5)
        self.list_btns["E2"]= self.E2

        self.E3 = Button(self.frame_buttons, text = "E3", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("E3"))
        self.E3.grid(padx=0,  pady=0, row=1, column=6)
        self.list_btns["E3"]= self.E3

        self.F1 = Button(self.frame_buttons, text = "F1", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("F1"))
        self.F1.grid(padx=(25,0),  pady=0, row=1, column=7)
        self.list_btns["F1"]= self.F1

        self.F2 = Button(self.frame_buttons, text = "F2", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("F2"))
        self.F2.grid(padx=0,  pady=0, row=2, column=0)
        self.list_btns["F2"]= self.F2

        self.F3 = Button(self.frame_buttons, text = "F3", font=f6, bg="goldenrod1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("F3"))
        self.F3.grid(padx=0,  pady=0, row=2, column=1)
        self.list_btns["F3"]= self.F3

        self.G1 = Button(self.frame_buttons, text = "G1", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("G1"))
        self.G1.grid(padx=0,  pady=(55,25), row=3, column=0)
        self.list_btns["G1"]= self.G1

        self.G2 = Button(self.frame_buttons, text = "G2", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("G2"))
        self.G2.grid(padx=0,  pady=(55,25), row=3, column=1)
        self.list_btns["G2"]= self.G2

        self.G3 = Button(self.frame_buttons, text = "G3", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("G3"))
        self.G3.grid(padx=0,  pady=(55,25), row=3, column=2)
        self.list_btns["G3"]= self.G3

        self.H1 = Button(self.frame_buttons, text = "H1", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("H1"))
        self.H1.grid(padx=0,  pady=(55,25), row=3, column=3)
        self.list_btns["H1"]= self.H1

        self.H2 = Button(self.frame_buttons, text = "H2", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("H2"))
        self.H2.grid(padx=0,  pady=(55,25), row=3, column=4)
        self.list_btns["H2"]= self.H2

        self.H3 = Button(self.frame_buttons, text = "H3", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("H3"))
        self.H3.grid(padx=0,  pady=(55,25), row=3, column=5)
        self.list_btns["H3"]= self.H3

        self.I1 = Button(self.frame_buttons, text = "I1", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("I1"))
        self.I1.grid(padx=0,  pady=(55,25), row=3, column=6)
        self.list_btns["I1"]= self.I1

        self.I2 = Button(self.frame_buttons, text = "I2", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("I2"))
        self.I2.grid(padx=(25,0),  pady=(55,25), row=3, column=7)
        self.list_btns["I2"]= self.I2

        self.I3 = Button(self.frame_buttons, text = "I3", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("I3"))
        self.I3.grid(padx=0,  pady=0, row=4, column=0)
        self.list_btns["I3"]= self.I3

        self.J1 = Button(self.frame_buttons, text = "J1", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("J1"))
        self.J1.grid(padx=0,  pady=0, row=4, column=1)
        self.list_btns["J1"]= self.J1

        self.J2 = Button(self.frame_buttons, text = "J2", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("J2"))
        self.J2.grid(padx=0,  pady=0, row=4, column=2)
        self.list_btns["J2"]= self.J2

        self.J3 = Button(self.frame_buttons, text = "J3", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("J3"))
        self.J3.grid(padx=0,  pady=0, row=4, column=3)
        self.list_btns["J3"]= self.J3

        self.J4 = Button(self.frame_buttons, text = "J4", font=f6, bg="tomato",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("J4"))
        self.J4.grid(padx=0,  pady=0, row=4, column=4)
        self.list_btns["J4"]= self.J4

        self.K1 = Button(self.frame_buttons, text = "K1", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("K1"))
        self.K1.grid(padx=0,  pady=(55,25), row=5, column=0)
        self.list_btns["K1"]= self.K1

        self.K2 = Button(self.frame_buttons, text = "K2", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("K2"))
        self.K2.grid(padx=0,  pady=(55,25), row=5, column=1)
        self.list_btns["K2"]= self.K2

        self.K3 = Button(self.frame_buttons, text = "K3", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("K3"))
        self.K3.grid(padx=0,  pady=(55,25), row=5, column=2)
        self.list_btns["K3"]= self.K3

        self.K4 = Button(self.frame_buttons, text = "K4", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("K4"))
        self.K4.grid(padx=0,  pady=(55,25), row=5, column=3)
        self.list_btns["K4"]= self.K4

        self.L1 = Button(self.frame_buttons, text = "L1", font=f6, bg="MediumPurple1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("L1"))
        self.L1.grid(padx=0,  pady=(55,25), row=5, column=4)
        self.list_btns["L1"]= self.L1

        self.L2 = Button(self.frame_buttons, text = "L2", font=f6, bg="MediumPurple1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("L2"))
        self.L2.grid(padx=0,  pady=(55,25), row=5, column=5)
        self.list_btns["L2"]= self.L2

        self.L3 = Button(self.frame_buttons, text = "L3", font=f6, bg="MediumPurple1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("L3"))
        self.L3.grid(padx=0,  pady=(55,25), row=5, column=6)
        self.list_btns["L3"]= self.L3

        self.L4 = Button(self.frame_buttons, text = "L4", font=f6, bg="MediumPurple1",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("L4"))
        self.L4.grid(padx=(25,0),  pady=(55,25), row=5, column=7)
        self.list_btns["L4"]= self.L4

        self.M1 = Button(self.frame_buttons, text = "M1", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("M1"))
        self.M1.grid(padx=0,  pady=0, row=6, column=0)
        self.list_btns["M1"]= self.M1

        self.M2 = Button(self.frame_buttons, text = "M2", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("M2"))
        self.M2.grid(padx=0,  pady=0, row=6, column=1)
        self.list_btns["M2"]= self.M2

        self.PP1 = Button(self.frame_buttons, text = "PP1", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("PP1"))
        self.PP1.grid(padx=0,  pady=(55,0), row=7, column=0)
        self.list_btns["PP1"]= self.PP1

        self.PP2 = Button(self.frame_buttons, text = "PP2", font=f6, bg="light sea green",\
                    height=2, width=3, bd=3, command = lambda: self.click_machines("PP2"))
        self.PP2.grid(padx=0,  pady=(55,0), row=7, column=1)
        self.list_btns["PP2"]= self.PP2

#====================================================treeview================================================
        # style for column names
        self.style = ttk.Style()
        # style for the body of the treeview.
        self.style.configure("mystyle1.Treeview", rowheight=42, font=f6)
        self.style.map("mystyle1.Treeview", background=[('selected', 'blue')])
        self.style.theme_use("default")
        self.style.configure("mystyle1.Treeview.Heading", font=f4)

        # TreeView
        self.tree_weight = ttk.Treeview(self.frame_weight, height=22, style="mystyle1.Treeview", selectmode='browse')
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
       
        
        # DB
        rolls = []
        for a in range(1,100):
            rolls.append((a, '05K/A', "{:.2f}" .format(13.5*(0.9+random()*0.2),2)))

        for i in range(len(rolls)):
            if i % 2 == 0:
                self.tree_weight.insert('', 'end', values=rolls[i], tags = ('odd',))
            else:
                self.tree_weight.insert('', 'end', values=rolls[i], tags = ('even',))



        # labels in stacker========================================================
        self.article = StringVar()

        self.label_date = Label(self.frame_labels, text="DATE",\
            font = f2).grid(row=0, column=0, sticky = 'w')
        self.label_dot1 = Label(self.frame_labels, text=":",\
            font = f2).grid(row=0, column=1, padx=(10,0))

        self.label_Equipe = Label(self.frame_labels, text="EQUIPE", \
            font = f2).grid(row=1, column=0, sticky = 'w', pady=30)
        self.label_dot2 = Label(self.frame_labels, text=":",\
            font = f2).grid(row=1, column=1, padx=(10,0), pady=30)

        self.label_machine = Label(self.frame_labels, text="MACHINE", \
            font = f2).grid(row=2, column=0, sticky = 'w')
        self.label_dot3 = Label(self.frame_labels, text=":",\
            font = f2).grid(row=2, column=1, padx=(10,0))

        self.label_production = Label(self.frame_labels, text="ID", \
            font = f2).grid(row=3, column=0, sticky = 'w', pady=30)
        self.label_dot4 = Label(self.frame_labels, text=":",\
            font = f2).grid(row=3, column=1, padx=(10,0), pady=30)

        self.label_article = Label(self.frame_labels, text="ARTICLE", \
            font = f2).grid(row=4, column=0, sticky = 'w')
        self.label_dot5 = Label(self.frame_labels, text=":",\
            font = f2).grid(row=4, column=1, padx=(10,0))

        articles=["","05K/A", "05NK/G","08D", "08NK/G"]
        self.combo_article = ttk.Combobox(self.frame_labels, width=17, textvariable=self.article,\
            values=articles,font = f2, state="readonly", justify="center")
        self.combo_article.grid(row=4, column=2, padx=20)

        self.label_poid = Label(self.frame_labels, text="POID", \
            font = f2).grid(row=5, column=0, sticky = 'w', pady=30)
        self.label_dot6 = Label(self.frame_labels, text=":",\
            font = f2).grid(row=5, column=1, padx=(10,0), pady=30)
        self.label_kg = Label(self.frame_labels, text="kg", \
            font = f2).grid(row=5, column=3, pady=15)

        # Entry
        self.ent_date = Entry(self.frame_labels, font = f2, width=18, bd=3,\
            justify='center', disabledbackground="lemon chiffon", disabledforeground="black")
        self.ent_date.grid(row=0, column=2)
        self.ent_date.insert(0, default_data.get("date"))
        self.ent_date.config(state='disabled')

        self.ent_equipe = Entry(self.frame_labels, font = f2, width=18, bd=3,\
            justify='center', disabledbackground="lemon chiffon", disabledforeground="black")
        self.ent_equipe.grid(row=1, column=2, pady=30)
        self.ent_equipe.insert(0, default_data.get("equipe"))
        self.ent_equipe.config(state='disabled')

        self.ent_machine = Entry(self.frame_labels, font = f2, width=18, bd=3,\
            justify='center', state='disabled', disabledbackground="lemon chiffon",\
            disabledforeground="black")
        self.ent_machine.grid(row=2, column=2)

        self.ent_id = Entry(self.frame_labels, font = f2, width=18, bd=3,\
            justify='center', state='disabled', disabledbackground="lemon chiffon",\
            disabledforeground="black")
        self.ent_id.grid(row=3, column=2, pady=30)

        self.poid_var = StringVar()
        self.ent_weight = Entry(self.frame_labels, font = f2, width=18, bd=3,\
            justify='center', textvariable=self.poid_var)
        self.ent_weight.grid(row=5, column=2, pady=15)

        # when choosing a thing of treeview
        def selecting(event):
            for info in self.tree_weight.selection():
                items = self.tree_weight.item(info)
                self.ent_id.config(state='normal')
                self.ent_id.delete(0, END)
                self.ent_id.insert(0, items['values'][0])
                self.ent_id.config(state='disabled')
                self.ent_weight.delete(0, END)
                self.ent_weight.insert(0, items['values'][2])
                self.combo_article.set(items['values'][1])

        self.tree_weight.bind('<<TreeviewSelect>>', selecting)

    def access(self):
        self.master.destroy()
        root = Tk()
        window1(root)

    # when click a button of machines
    def click_machines(self, group):
        for M, V in self.list_btns.items():
            if M == group:
                V.config(bg = 'green2')
            else:
                if M in self.color1:
                    V.config(bg="goldenrod1")
                elif M in self.color2:
                    V.config(bg="tomato")
                elif M in self.color3:
                    V.config(bg="light sea green")
                elif M in self.color4:
                    V.config(bg="MediumPurple1")
        
        self.ent_machine.config(state='normal')
        self.ent_machine.delete(0, END)
        self.ent_machine.insert(0, group)
        self.ent_machine.config(state='disabled')

    def setting_articles(self):
        import articles
        articles.a(self)
        #pop_article = Toplevel(self.master)
        #popup_articles(pop_article)

'''
        self.articles = Toplevel(self.master)
        self.articles.geometry('1000x720+455+100')
        self.articles.title('Les articles')
        
        # Frames =============
        self.baseFrame = Frame(self.articles)
        self.baseFrame.pack()

        self.lblFrame_articles = LabelFrame(self.baseFrame, text="list des articles")
        self.lblFrame_articles.grid(row=0, column=0)
        self.lblFrame_modif = LabelFrame(self.baseFrame, text = "modification")
        self.lblFrame_modif.grid(row=1, column=0)
        self.lblFrame_enFab = LabelFrame(self.baseFrame, text = "en fabrication")
        self.lblFrame_enFab.grid(row=2, column=0)
        # Treeview============
        self.tree_articles = ttk.Treeview(self.lblFrame_articles, height=22)
        self.tree_articles['columns'] = ("article", "poid produit", "largeur", "longueur",\
        "quantité(pcs)", "poid emballage", "poid sac", "épaisseur" , "poid 1m")
        self.style_articles = ttk.Style()
        self.style_articles.theme_use("default")
        self.style_articles.configure("Treeview.Heading", font=f4)
        self.style_articles.configure("mystyle.Treeview", rowwidth=10, font=f2)
        self.style_articles.map("Treeview", background=[('selected', 'blue')])
        self.tree_articles.pack()


        self.articles.grab_set()

class popup_articles:
    def __init__(self, master):

        self.master = master
        self.master.geometry('1000x720+455+100')
        self.master.title('Les articles')

        self.baseFrame = Frame(self.master)
        self.baseFrame.pack()
        self.lblFrame_articles = LabelFrame(self.baseFrame, text="list des articles")
        self.lblFrame_articles.grid(row=0, column=0)
        self.lblFrame_modif = LabelFrame(self.baseFrame, text = "modification")
        self.lblFrame_modif.grid(row=1, column=0)
        self.lblFrame_enFab = LabelFrame(self.baseFrame, text = "en fabrication")
        self.lblFrame_enFab.grid(row=2, column=0)

        self.tree_articles = ttk.Treeview(self.lblFrame_articles, height=22)
        self.tree_articles['columns'] = ("article", "poid produit", "largeur", "longueur",\
            "quantité(pcs)", "poid emballage", "poid sac", "épaisseur" , "poid 1m")
        self.style_articles = ttk.Style()
        self.style_articles.theme_use("default")
        self.style_articles.configure("Treeview.Heading", font=f4)
        self.style_articles.configure("mystyle.Treeview", rowwidth=10, font=f2)
        self.style_articles.map("Treeview", background=[('selected', 'blue')])
        
        self.tree_articles.pack()



        self.master.grab_set()

'''
                



if __name__ == '__main__':
    main()