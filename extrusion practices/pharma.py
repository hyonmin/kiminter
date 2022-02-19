from calendar import Calendar
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkcalendar import Calendar
import random
import time;
from datetime import datetime

def main():
    root = Tk()
    app = window1(root)
    root.mainloop()
    
class window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Kim International Stacker - E")
        self.master.geometry('1350x750+285+100')
        
        self.frame = Frame(self.master, bg='dodger blue')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()
#----------------------font-----------------------------
        f1 = ('times new roman', 50, 'bold')
        f2 = ('arial', 20, 'bold')
        #calendar
        f3 = ('arial', 18, 'bold')
#----------------------frames---------------------------
        self.LabelTitle = Label(self.frame, text = 'Kim International Stacker - E',\
            bg='dodger blue', foreground='white', font=f1, bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.Loginframe1 = LabelFrame(self.frame, text = "Calendrier", bg='dodger blue',\
            width=500, height=300, bd=5, relief='ridge', font=f2, padx=25, pady=25)
        self.Loginframe1.grid(row=1, column=0, rowspan=2, padx=50, pady=50)
        
        self.Loginframe2 = LabelFrame(self.frame, text = "Equipe", bg='dodger blue',\
            width=500, height=100, bd=5, relief='ridge', font=f2)
        self.Loginframe2.grid(row=1, column=1)
        
        self.Loginframe3 = LabelFrame(self.frame, text = "Jour / Soir", bg='dodger blue',\
            width=500, height=200, bd=5, relief='ridge', font=f2)
        self.Loginframe3.grid(row=2, column=1)

#----------------------entries on frame1--------------------------------

        self.lblUsername = Label(self.Loginframe1, text = 'Username', bg='dodger blue',\
            font=f2, bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.Loginframe1,\
            font=f2, textvariable=self.Username, bd=2)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.Loginframe1, text = 'Password', bg='dodger blue',\
            font=f2, bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.Loginframe1,\
            font=f2, textvariable=self.Password, bd=2)
        self.txtPassword.grid(row=1, column=1)

#--------------------button on frame2----------------------
        self.btnlogin = Button(self.Loginframe2, text = "Login", width=17,\
            font=f3, command = self.login_System)
        self.btnlogin.grid(row=0, column=0)

        self.btnReset = Button(self.Loginframe2, text = "Reset", width=17,\
            font=f3, command = self.Reset)
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(self.Loginframe2, text = "Exit", width=17,\
            font=f3, command = self.iExit)
        self.btnExit.grid(row=0, column=2)
#--------------------button on frame3----------------------
        self.btnRegistration = Button(self.Loginframe3, text = "Patients Registration System",\
            state=DISABLED, font=f3, command = self.Registration_window)
        self.btnRegistration.grid(row=0, column=0)

        self.btnHospital = Button(self.Loginframe3, text = 'Hospital Management System',\
            state=DISABLED, font=f3, command = self.Hospital_window)
        self.btnHospital.grid(row=0, column=1, pady=8, padx=22)
#-----------------------------------------------------------
        
    
    def login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())

        if (user == str(1234)) and (pas == str(2345)):
            self.btnRegistration.config(state=NORMAL)
            self.btnHospital.config(state=NORMAL)
        else:
            tkinter.messagebox.showerror("Pharmacy Management System", "You have entered an invalid login details.")
            self.btnRegistration.config(state=DISABLED)
            self.btnHospital.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
    
    def Reset(self):
        self.btnRegistration.config(state=DISABLED)
        self.btnHospital.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Pharmacy Management System", "Confirm if you want to exit.")
        if self.iExit > 0:
            self.master.destroy()
            return

    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window3(self.newWindow)

class window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patients Registration System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


class window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == '__main__':
    main()