from tkinter import *
import tkinter.messagebox
import stdDatabase


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x750")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #=====================function========================
        def iexit():
            iexit = tkinter.messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")
            if iexit > 0:
                root.destroy()
                return
        
        def clearData():
            self.txtStdID.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAdr.delete(0, END)
            self.txtMobile.delete(0, END)

        def addData():
            if(len(StdID.get()) !=0 ):
                stdDatabase.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(),\
                    Age.get(), Gender.get(), Address.get(), Mobile.get())

                studentlist.delete(0, END)

                studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(),\
                    Age.get(), Gender.get(), Address.get(), Mobile.get()))
        def DisplayData():
            studentlist.delete(0, END)
            for row in stdDatabase.viewData():
                studentlist.insert(END, row)

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)
            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sd[2])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sd[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[6])
            self.txtAdr.delete(0, END)
            self.txtAdr.insert(END, sd[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[8])

        def DeleteData():
            if(len(StdID.get()) !=0 ):
                stdDatabase.deleteRec(sd[0])
                clearData()
                DisplayData()
        def searchDatebase():
            studentlist.delete(0,END)
            for row in stdDatabase.searchDate(StdID.get(), Firstname.get(), Surname.get(), DoB.get(),\
                Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentlist.insert(END, row, str(""))
        def update():
            if(len(StdID.get()) !=0 ):
                stdDatabase.deleteRec(sd[0])
            if(len(StdID.get()) !=0 ):
                stdDatabase.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(),\
                    Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), Firstname.get(), Surname.get(), DoB.get(),\
                    Age.get(), Gender.get(), Address.get(), Mobile.get()))
            



        #======================default settings============================
        # titles
        f1=('arial', 47, 'bold')
        f2=('arial', 20, 'bold')
        f3=('arial', 12, 'bold')

        #============================Frames=================================
        mainFrame = Frame(self.root, bg="cadet blue")
        mainFrame.grid()

        titleFrame = Frame(mainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        titleFrame.pack(side=TOP)

        self.lblTitle = Label(titleFrame, font = f1, text = "Student Database Management System",\
            bg = "Ghost White")
        self.lblTitle.grid()

        buttonFrame = Frame(mainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White",\
            relief=RIDGE)
        buttonFrame.pack(side=BOTTOM)
        dataFrame = Frame(mainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,\
            bg="cadet blue")
        dataFrame.pack(side=BOTTOM)
        dataFrameLEFT = LabelFrame(dataFrame, bd=1, width=1000, height=600, padx=20,\
            relief=RIDGE, bg="Ghost White", text="Student Info\n", font=f2)
        dataFrameLEFT.pack(side=LEFT)
        dataFrameRIGHT = LabelFrame(dataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,\
            bg="Ghost White", text="Student Details\n", font=f2)
        dataFrameRIGHT.pack(side=RIGHT)
        #========================Labels, Entries=======================
        self.lblStdID = Label(dataFrameLEFT, font=f2, text="Student ID: ", padx=2, pady=2, bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(dataFrameLEFT, font=f2, textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblfna = Label(dataFrameLEFT, font=f2, text="Firstname: ", padx=2, pady=2, bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(dataFrameLEFT, font=f2, textvariable=Firstname, width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(dataFrameLEFT, font=f2, text="Surname: ", padx=2, pady=2, bg="Ghost White")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(dataFrameLEFT, font=f2, textvariable=Surname, width=39)
        self.txtSna.grid(row=2, column=1)

        self.lblDoB = Label(dataFrameLEFT, font=f2, text="Date of Birth: ", padx=2, pady=2, bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(dataFrameLEFT, font=f2, textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(dataFrameLEFT, font=f2, text="Age: ", padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(dataFrameLEFT, font=f2, textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(dataFrameLEFT, font=f2, text="Gender: ", padx=2, pady=2, bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(dataFrameLEFT, font=f2, textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblAdr = Label(dataFrameLEFT, font=f2, text="Address: ", padx=2, pady=2, bg="Ghost White")
        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.txtAdr = Entry(dataFrameLEFT, font=f2, textvariable=Address, width=39)
        self.txtAdr.grid(row=6, column=1)

        self.lblMobile = Label(dataFrameLEFT, font=f2, text="Mobile: ", padx=2, pady=2, bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(dataFrameLEFT, font=f2, textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)
        #===============================Listbox & ScrollBar Widget=================
        scrollbar = Scrollbar(dataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(dataFrameRIGHT, width=41, height=16, font=f3,\
            yscrollcommand=scrollbar.set)
        studentlist.bind("<<ListboxSelect>>", StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)
        #====================================buttons==================================
        self.btnAddDate = Button(buttonFrame, text="Add New", font=f2, height=1, width=10, bd=4,\
            command=addData)
        self.btnAddDate.grid(row=0, column=0)
        self.btnDisplayData = Button(buttonFrame, text="Display", font=f2, height=1, width=10, bd=4,\
            command= DisplayData)
        self.btnDisplayData.grid(row=0, column=1)
        self.btnClearData = Button(buttonFrame, text="ClearData", font=f2, height=1, width=10, bd=4,\
            command =clearData)
        self.btnClearData.grid(row=0, column=2)
        self.btnDeleteData = Button(buttonFrame, text="Delete", font=f2, height=1, width=10, bd=4,\
            command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)
        self.btnSearchData = Button(buttonFrame, text="Search", font=f2, height=1, width=10, bd=4,\
            command = searchDatebase)
        self.btnSearchData.grid(row=0, column=4)
        self.btnUpdateData = Button(buttonFrame, text="Update", font=f2, height=1, width=10, bd=4,\
            command = update)
        self.btnUpdateData.grid(row=0, column=5)
        self.btnExit = Button(buttonFrame, text="Exit", font=f2, height=1, width=10, bd=4,\
            command=iexit)
        self.btnExit.grid(row=0, column=6)

if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()