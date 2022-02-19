from tkinter import *
from tkcalendar import *
import sqlite3
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time

def main():
    root = Tk()
    application = studentRecords(root)
    root.mainloop()

class studentRecords:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record System")
        self.root.geometry("1350x700")

        notebook = ttk.Notebook(self.root)
        self.TabControl1 = ttk.Notebook(self.root)
        self.TabControl2 = ttk.Notebook(self.root)
        self.TabControl3 = ttk.Notebook(self.root)
        notebook.add(self.TabControl1, text="School System")
        notebook.add(self.TabControl2, text="School Detail")
        notebook.grid()

        #================================variables======================
        self.StudentID = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.Address = StringVar()
        self.PostCode = StringVar()
        self.Gender = StringVar()
        self.DOB = StringVar()
        self.Mobile = StringVar()
        self.Email = StringVar()

        self.ParentGuidance = StringVar()
        self.pgFirstname = StringVar()
        self.pgSurname = StringVar()
        self.pgAddress = StringVar()
        self.pgWorkPhone = StringVar()
        self.pgMobile = StringVar()
        self.pgEmail = StringVar()
        
        self.Course = StringVar()
        self.CourseCode = StringVar()
        self.Faculty = StringVar()
        self.Dean = StringVar()
        self.Head_of_School = StringVar()
        self.ProgramLeader = StringVar()
        self.CourseTutor = StringVar()
        self.Building = StringVar()
        
        self.HomeStudent = StringVar()
        self.Oversea = StringVar()
        self.Accommodation = StringVar()
        self.ExchageProg = StringVar()
        self.Scholarship = StringVar()

        self.BA = StringVar()
        self.BSc = StringVar()
        self.MA = StringVar()
        self.MSc = StringVar()
        self.PhD = StringVar()

        self.DataScience = StringVar()
        self.EventDrivenPro = StringVar()
        self.ObjectOriented = StringVar()
        self.Spreadsheet = StringVar()
        self.SystemAnalysis = StringVar()
        self.InformTechnology = StringVar()
        self.DigitalGraphics = StringVar()

        self.English = StringVar()
        self.Games = StringVar()
        self.Animation = StringVar()
        self.Database = StringVar()
        self.Maths = StringVar()
        self.AddMaths = StringVar()
        self.Physics = StringVar()
        self.Media = StringVar()
        self.Graphics = StringVar()
        
        self.ScoreMaths = StringVar()
        self.ScoreEnglish = StringVar()
        self.ScoreBiology = StringVar()
        self.ScoreComputing = StringVar()
        self.ExamNo = StringVar()
        self.ScoreChemistry = StringVar()
        self.ScorePhysics = StringVar()
        self.ScoreAddMaths = StringVar()
        self.ScoreBusiness = StringVar()
        self.TotalScore = StringVar()
        self.Average = StringVar()
        self.Ranking = StringVar()
        self.TaxPeriod = StringVar()
        self.iDate = StringVar()

        self.Module1 = StringVar()
        self.Module2 = StringVar()
        self.Module3 = StringVar()
        self.Module4 = StringVar()
        self.Module5 = StringVar()
        self.Module6 = StringVar()
        self.Module7 = StringVar()
        self.Module8 = StringVar()
        self.ResultDate = StringVar()

        self.Subject1 = StringVar()
        self.Subject2 = StringVar()
        self.Subject3 = StringVar()
        self.Subject4 = StringVar()
        self.Subject5 = StringVar()
        self.Subject6 = StringVar()
        self.Subject7 = StringVar()
        self.Subject8 = StringVar()
        #=========================exit================================
        def iExit():
            iExit = tkinter.messagebox.askyesno('Student Management System', 'Confirm if you want to exit.')
            if iExit > 0:
                root.destroy()
                return

        #=====================================================reset========
        def Reset():
            self.StudentID.set("")
            self.Firstname.set("")
            self.Surname.set("")
            self.Address.set("")
            self.PostCode.set("")
            self.Gender.set("")
            self.DOB.set("")
            self.Mobile.set("")
            self.Email.set("")

            self.ParentGuidance.set("")
            self.pgFirstname.set("")
            self.pgSurname.set("")
            self.pgAddress.set("")
            self.pgWorkPhone.set("")
            self.pgMobile.set("")
            self.pgEmail.set("")

            self.Course.set("Course Selector")
            self.CourseCode.set("")
            self.Faculty.set("")
            self.Dean.set("")
            self.Head_of_School.set("")
            self.ProgramLeader.set("")
            self.CourseTutor.set("")
            self.Building.set("")
            
            self.HomeStudent.set("No")
            self.Oversea.set("No")
            self.Accommodation.set("No")
            self.ExchageProg.set("No")
            self.Scholarship.set("No")

            self.BA.set("0")
            self.BSc.set("0")
            self.MA.set("0")
            self.MSc.set("0")
            self.PhD.set("0")

            self.DataScience.set("No")
            self.EventDrivenPro.set("No")
            self.ObjectOriented.set("No")
            self.Spreadsheet.set("No")
            self.SystemAnalysis.set("No")
            self.InformTechnology.set("No")
            self.DigitalGraphics.set("No")

            self.English.set("No")
            self.Games.set("No")
            self.Animation.set("No")
            self.Database.set("No")
            self.Maths.set("No")
            self.AddMaths.set("No")
            self.Physics.set("No")
            self.Media.set("No")
            self.Graphics.set("No")

            self.Subject1.set("")
            self.Subject2.set("")
            self.Subject3.set("")
            self.Subject4.set("")
            self.Subject5.set("")
            self.Subject6.set("")
            self.Subject7.set("")
            self.Subject8.set("")

            self.TotalScore.set("")
            self.Ranking.set("")
            self.ResultDate.set("")

            self.Module1.set("")
            self.Module2.set("")
            self.Module3.set("")
            self.Module4.set("")
            self.Module5.set("")
            self.Module6.set("")
            self.Module7.set("")
            self.Module8.set("")
        
        #=======================================================
        def setSubject(event):
            if self.Subject1.get() == 'Event Driven Prog':
                self.EventDrivenPro.set("Core Unit")
                self.txt1.configure(state=NORMAL)
                self.txt1.focus_set()
            elif self.Subject1.get() == '':
                self.EventDrivenPro.set("No")
                self.txt1.configure(state=DISABLED)
                self.Module1.set("")

            if self.Subject2.get() == 'Object Oriented':
                self.ObjectOriented.set("Complete")
                self.Spreadsheet.set("No")
                self.txt2.configure(state=NORMAL)
                self.txt2.focus_set()
            if self.Subject2.get() == 'SpreadSheet':
                self.ObjectOriented.set("No")
                self.Spreadsheet.set("Core Unit")
                self.txt2.configure(state=NORMAL)
                self.txt2.focus_set()
            elif self.Subject2.get() == '':
                self.ObjectOriented.set("No")
                self.Spreadsheet.set("No")
                self.txt2.configure(state=DISABLED)
                self.Module2.set("")

            if self.Subject3.get() == 'System Analysis':
                self.SystemAnalysis.set("Core Unit")
                self.Spreadsheet.set("No")
                self.txt3.configure(state=NORMAL)
                self.txt3.focus_set()
            if self.Subject3.get() == 'Inform Technology':
                self.InformTechnology.set("Core Unit")
                self.SystemAnalysis.set("No")
                self.txt3.configure(state=NORMAL)
                self.txt3.focus_set()
            elif self.Subject3.get() == '':
                self.InformTechnology.set("No")
                self.SystemAnalysis.set("No")
                self.txt3.configure(state=DISABLED)
                self.Module3.set("")

            if self.Subject4.get() == 'Digital Graphics':
                self.DigitalGraphics.set("Complete")
                self.English.set("No")
                self.txt4.configure(state=NORMAL)
                self.txt4.focus_set()
            if self.Subject4.get() == 'English':
                self.English.set("Core Unit")
                self.DigitalGraphics.set("No")
                self.txt4.configure(state=NORMAL)
                self.txt4.focus_set()
            elif self.Subject4.get() == '':
                self.English.set("No")
                self.DigitalGraphics.set("No")
                self.txt4.configure(state=DISABLED)
                self.Module4.set("")

            if self.Subject5.get() == 'Games':
                self.Games.set("Complete")
                self.Animation.set("No")
                self.txt5.configure(state=NORMAL)
                self.txt5.focus_set()
            if self.Subject5.get() == 'Animation':
                self.Animation.set("Complete")
                self.Games.set("No")
                self.txt5.configure(state=NORMAL)
                self.txt5.focus_set()
            elif self.Subject5.get() == '':
                self.Animation.set("No")
                self.Games.set("No")
                self.txt5.configure(state=DISABLED)
                self.Module5.set("")
            
            if self.Subject6.get() == 'Database':
                self.Database.set("Complete")
                self.Maths.set("No")
                self.txt6.configure(state=NORMAL)
                self.txt6.focus_set()
            if self.Subject6.get() == 'Maths':
                self.Maths.set("Core Unit")
                self.Database.set("No")
                self.txt6.configure(state=NORMAL)
                self.txt6.focus_set()
            elif self.Subject6.get() == '':
                self.Maths.set("No")
                self.Animation.set("No")
                self.txt6.configure(state=DISABLED)
                self.Module6.set("")

            if self.Subject7.get() == 'AddMaths':
                self.AddMaths.set("Complete")
                self.Physics.set("No")
                self.txt7.configure(state=NORMAL)
                self.txt7.focus_set()
            if self.Subject7.get() == 'Physics':
                self.AddMaths.set("No")
                self.Physics.set("Core Unit")
                self.txt7.configure(state=NORMAL)
                self.txt7.focus_set()
            elif self.Subject7.get() == '':
                self.Physics.set("No")
                self.AddMaths.set("No")
                self.txt7.configure(state=DISABLED)
                self.Module7.set("")

            if self.Subject8.get() == 'Data Science':
                self.DataScience.set("Core Unit")
                self.txt8.configure(state=NORMAL)
                self.txt8.focus_set()
            elif self.Subject8.get() == '':
                self.DataScience.set("No")
                self.txt8.configure(state=DISABLED)
                self.Module8.set("")

        #========================
        def CourseData(event):
            if self.Course.get() == 'BSc Serious Game':
                self.CourseCode.set('BScGS354')
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Folake Tomiola")
                self.Head_of_School.set("Dunny Tony Jonathan")
                self.ProgramLeader.set("Dr. Peter Stone")
                self.CourseTutor.set("Dr. Rose Royce")
                self.Building.set("Kelly's House")

            if self.Course.get() == 'BSc Computer Science':
                self.CourseCode.set('BScCS01')
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Tony Montana")
                self.Head_of_School.set("Dunny Tony Jonathan")
                self.ProgramLeader.set("Dr. Femi Lagos")
                self.CourseTutor.set("Dr. Paul Parker")
                self.Building.set("Bishop's House")

            if self.Course.get() == 'BA Animation':
                self.CourseCode.set('BAA01')
                self.Faculty.set("School of Art")
                self.Dean.set("Prof. Sally Whymore")
                self.Head_of_School.set("Prof. Peter Parker")
                self.ProgramLeader.set("Dr. Helen Forngnal")
                self.CourseTutor.set("Dr. Rebecca Okon")
                self.Building.set("Art Block")

            if self.Course.get() == 'BSc Information System':
                self.CourseCode.set('BScIS01')
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Tony Montana")
                self.Head_of_School.set("Dr. Raja Khan")
                self.ProgramLeader.set("Dr. Victor Warlord")
                self.CourseTutor.set("Dr. Kemi Adewale")
                self.Building.set("Tony Allen")
            
            if self.Course.get() == 'BSc Computing':
                self.CourseCode.set('BScC01')
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Tony Montana")
                self.Head_of_School.set("Dr. Sunny Jonathan")
                self.ProgramLeader.set("Dr. James Townsend")
                self.CourseTutor.set("Dr. Felix Wales")
                self.Building.set("Kilburn Corner")

            if self.Course.get() == 'BSc Computer Game':
                self.CourseCode.set('BScCG01')
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Tony Montana")
                self.Head_of_School.set("Dr. Sunny Jonathan")
                self.ProgramLeader.set("Dr. Grace Goldsmith")
                self.CourseTutor.set("Dr. Goodman Hall")
                self.Building.set("Bishop's House")

            if self.Course.get() == 'BSc Computer Animation':
                self.CourseCode.set('BScCG01')
                self.Faculty.set("School of Creative Art and Science")
                self.Dean.set("Prof. Paulin Peters")
                self.Head_of_School.set("Dr. Fatin Johnson")
                self.ProgramLeader.set("Dr. Meryem Holyway")
                self.CourseTutor.set("Dr. Malachy Ahmed")
                self.Building.set("Joseph's House")

        def AddModulescore():
            if self.Module1.get() == "":
                self.Module1.set("0")
            if self.Module2.get() == "":
                self.Module2.set("0")
            if self.Module3.get() == "":
                self.Module3.set("0")
            if self.Module4.get() == "":
                self.Module4.set("0")
            if self.Module5.get() == "":
                self.Module5.set("0")
            if self.Module6.get() == "":
                self.Module6.set("0")
            if self.Module7.get() == "":
                self.Module7.set("0")
            if self.Module8.get() == "":
                self.Module8.set("0")
            
            Unit1 = float(self.Module1.get())
            Unit2 = float(self.Module2.get())
            Unit3 = float(self.Module3.get())
            Unit4 = float(self.Module4.get())
            Unit5 = float(self.Module5.get())
            Unit6 = float(self.Module6.get())
            Unit7 = float(self.Module7.get())
            Unit8 = float(self.Module8.get())

            UnitTotal = Unit1 + Unit2 + Unit3 + Unit4 + Unit5 + Unit6 + Unit7 + Unit8
            self.TotalScore.set(int(UnitTotal))

            if UnitTotal >= 700:
                self.Ranking.set('1st Class')
            elif UnitTotal >= 600:
                self.Ranking.set('2.i Upper')
            elif UnitTotal >= 500:
                self.Ranking.set('2.ii Lower')
            elif UnitTotal >= 400:
                self.Ranking.set('3rd Class')
            elif UnitTotal >= 300:
                self.Ranking.set('CoHE')
            elif UnitTotal <= 300:
                self.Ranking.set('Fail')

        #=======================Data con==============================
        #def addData():
        #    if self.StudentID.get() == "" or self.Firstname.get() == "" or self.Surname.get() == "":
        #        tkinter.messagebox.showerror("Enter correct members details")
        #   else:
                

        



        #========================frames===============================
        MainFrame = Frame(self.TabControl1, bd=10, width=1350, height=700, relief = RIDGE)
        MainFrame.grid(padx=5, pady=10)

        Tab2Frame = Frame(self.TabControl2, bd=10, width=1350, height=700, relief = RIDGE)
        Tab2Frame.grid(padx=5, pady=10)

        TopFrame3 = Frame(MainFrame, bd=10, width=1340, height=500, relief = RIDGE)
        TopFrame3.grid(padx=5, pady=10)
        TopFrame2 = Frame(MainFrame, bd=10, width=1340, height=500, relief = RIDGE)
        TopFrame2.grid(padx=5, pady=10)
        TopFrame1 = Frame(MainFrame, bd=10, width=1340, height=500, relief = RIDGE)
        TopFrame1.grid(padx=5, pady=10)

        RightFrame1 = Frame(TopFrame3, bd=5, width=320, height=400, padx=2,\
            bg = 'cadetblue',relief = RIDGE)
        RightFrame1.pack(side=RIGHT, pady=1)

        InnerRightFrame = Frame(RightFrame1, bd=5, width=310, height=300, padx=2, relief = RIDGE)
        InnerRightFrame.pack(side=TOP, pady=2)

        CalendarFrame = Frame(InnerRightFrame, bd=5, width=310, height=300, padx=3, relief = RIDGE)
        CalendarFrame.pack(side=TOP, pady=1)

        UnitsFrame = Frame(InnerRightFrame, bd=5, width=310, height=300, padx=2, relief = RIDGE)
        UnitsFrame.pack(side=TOP, pady=1)

        ResultFrame = Frame(InnerRightFrame, bd=5, width=330, height=50, padx=2, relief = RIDGE)
        ResultFrame.pack(side=TOP, pady=1)

        ResultFrameLeft = Frame(ResultFrame, relief = RIDGE)
        ResultFrameLeft.grid(row=0, column=0, pady=1)

        ResultFrameRight = Frame(ResultFrame, bd=0, width=200, height=50, padx=2, relief = RIDGE)
        ResultFrameRight.grid(row=0, column=1)

        UnitNo = Frame(UnitsFrame, bd=0, width=50, height=300, padx=2, relief =RIDGE)
        UnitNo.grid(row=0, column=0, pady=2)
        UnitSubject = Frame(UnitsFrame, bd=1, width=210, height=300, padx=2, pady=4, relief =RIDGE)
        UnitSubject.grid(row=0, column=1, pady=2)
        UnitScore = Frame(UnitsFrame, bd=0, width=50, height=300, padx=2, pady=3, relief =RIDGE)
        UnitScore.grid(row=0, column=2, pady=1)

        LeftFrame = Frame(TopFrame3, bd=5, width=1340, height=400, padx=2, bg="cadetblue", relief=RIDGE)
        LeftFrame.pack(side=RIGHT, pady=0)
        CourseFrame = Frame(LeftFrame, bd=5, width=600, height=180, padx=4, relief=RIDGE)
        CourseFrame.pack(side=TOP, pady=2)
        
        LeftFrame2 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2,bg="cadetblue", relief=RIDGE)
        LeftFrame2.pack(side=TOP)
        StudentStatusFrame = Frame(LeftFrame2, bd=5, width=300, height=170, padx=6, pady=0, relief=RIDGE)
        StudentStatusFrame.pack(side=LEFT, padx=0)
        DegreeFrame = Frame(LeftFrame2, bd=5, width=300, height=170, padx=6, relief=RIDGE)
        DegreeFrame.pack(side=RIGHT, padx=0)

        ButtonFrame = Frame(LeftFrame, bd=5, width=320, height=50, padx=4, relief=RIDGE)
        ButtonFrame.pack(side=LEFT)

        RightFrame2 = Frame(TopFrame3, bd=5, width=300, height=400, padx=2, bg="cadetblue", relief=RIDGE)
        RightFrame2.pack(side=LEFT, pady=5)
        StudentFrame = Frame(RightFrame2, bd=5, width=280, height=50, padx=2, relief=RIDGE)
        StudentFrame.pack(side=TOP, pady=3)
        ParentFrame = Frame(RightFrame2, bd=5, width=280, height=50, padx=3, relief=RIDGE)
        ParentFrame.pack(side=TOP)

        TopFrame11 = Frame(Tab2Frame, bd=10, width=1340, height=60, relief=RIDGE)
        TopFrame11.grid(row=0, column=0)
        TopFrame12 = Frame(Tab2Frame, bd=10, width=1340, height=100, relief=RIDGE)
        TopFrame12.grid(row=1, column=0)

        TopFrame12a = Frame(TopFrame12, bd=10, width=1000, height=100, relief=RIDGE)
        TopFrame12a.grid(row=1, column=1)
        TopFrame12b = Frame(TopFrame12, bd=10, width=340, height=100, relief=RIDGE)
        TopFrame12b.grid(row=1, column=0)
        #========================================================
        self.lblStudentID = Label(StudentFrame, font=("arial", 12, 'bold'), text='Student ID',\
            bd=7, anchor='w', justify=LEFT)
        self.lblStudentID.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtStudentID = Entry(StudentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=25, justify='left', textvariable=self.StudentID)
        self.txtStudentID.grid(row=0, column=1)

        self.lblFirstname = Label(StudentFrame, font=("arial", 12, 'bold'), text='Firstname',\
            bd=7, justify=LEFT)
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5)
        self.txtFirstname = Entry(StudentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=25, justify='left', textvariable=self.Firstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(StudentFrame, font=("arial", 12, 'bold'), text='Surname', bd=5)
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5)
        self.txtSurname = Entry(StudentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=25, textvariable=self.Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(StudentFrame, font=("arial", 12, 'bold'), text='Address', bd=5)
        self.lblAddress.grid(row=3, column=0, sticky=W, padx=5)
        self.txtAddress = Entry(StudentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=25, textvariable=self.Address)
        self.txtAddress.grid(row=3, column=1)

        self.lblPostCode = Label(StudentFrame, font=("arial", 12, 'bold'), text='Post Code', bd=5)
        self.lblPostCode.grid(row=4, column=0, sticky=W, padx=5)
        self.txtPostCode = Entry(StudentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=25, textvariable=self.PostCode)
        self.txtPostCode.grid(row=4, column=1)

        self.lblGender = Label(StudentFrame, font=("arial", 12, 'bold'), text='Gender', bd=5)
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5)

        self.cboGender = ttk.Combobox(StudentFrame, font=('arial', 12, 'bold'),\
            width=23, textvariable=self.Gender, state="readonly")
        self.cboGender['value'] = ('','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1)

        self.lblDOB = Label(StudentFrame, font=('arial', 12, 'bold'), text='DOB', bd=5)
        self.lblDOB.grid(row=6, column=0, sticky=W, padx=5)
        self.txtDOB = Entry(StudentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=25, textvariable=self.DOB)
        self.txtDOB.grid(row=6, column=1)

        self.lblMobile = Label(StudentFrame, font=('arial', 12, 'bold'), text='Mobile', bd=5)
        self.lblMobile.grid(row=7, column=0, sticky=W, padx=5)
        self.txtMobile = Entry(StudentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=25, textvariable=self.Mobile)
        self.txtMobile.grid(row=7, column=1)

        self.lblEmail = Label(StudentFrame, font=('arial', 12, 'bold'), text='Email', bd=5)
        self.lblEmail.grid(row=8, column=0, sticky=W, padx=5)
        self.txtEmail = Entry(StudentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=25, textvariable=self.Email)
        self.txtEmail.grid(row=8, column=1)
        
        #==============================Parents==========
        self.lblParentGuidance = Label(ParentFrame, font=('arial', 12, 'bold'),\
            text='Parent or Guidance', bd=5)
        self.lblParentGuidance.grid(row=0, column=0, sticky=W, padx=8)
        self.cboParentGuidance = ttk.Combobox(ParentFrame, font=('arial', 12, 'bold'),\
            width=16, textvariable=self.ParentGuidance, state="readonly")
        self.cboParentGuidance['value'] = ('','Mother','Father','Brother', 'Sister', 'Guidance')
        self.cboParentGuidance.current(0)
        self.cboParentGuidance.grid(row=0, column=1)

        self.lblFirstname = Label(ParentFrame, font=("arial", 12, 'bold'), text='Firstname',\
            bd=7, justify=LEFT)
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5)
        self.txtFirstname = Entry(ParentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=17, justify='left', textvariable=self.pgFirstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(ParentFrame, font=("arial", 12, 'bold'), text='Surname', bd=5)
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5)
        self.txtSurname = Entry(ParentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=17, textvariable=self.pgSurname)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(ParentFrame, font=("arial", 12, 'bold'), text='Address', bd=5)
        self.lblAddress.grid(row=3, column=0, sticky=W, padx=5)
        self.txtAddress = Entry(ParentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=17, textvariable=self.pgAddress)
        self.txtAddress.grid(row=3, column=1)

        self.lblWorkPhone = Label(ParentFrame, font=("arial", 12, 'bold'), text='Work Phone No', bd=5)
        self.lblWorkPhone.grid(row=4, column=0, sticky=W, padx=5)
        self.txtWorkPhone = Entry(ParentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=17, textvariable=self.pgWorkPhone)
        self.txtWorkPhone.grid(row=4, column=1)

        self.lblMobile = Label(ParentFrame, font=("arial", 12, 'bold'), text='Mobile', bd=5)
        self.lblMobile.grid(row=5, column=0, sticky=W, padx=5)
        self.txtMobile = Entry(ParentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=17, textvariable=self.pgMobile)
        self.txtMobile.grid(row=5, column=1)

        self.lblEmail = Label(ParentFrame, font=("arial", 12, 'bold'), text='Email', bd=5)
        self.lblEmail.grid(row=6, column=0, sticky=W, padx=5)
        self.txtEmail = Entry(ParentFrame, font=('arial', 12, 'bold'),\
            bd=5, width=17, textvariable=self.pgEmail)
        self.txtEmail.grid(row=6, column=1, pady=5)
        #================================self.Course=================================
        self.Course.set('Course Selector')
        self.lblCourse = Label(CourseFrame, font=('arial', 12, 'bold'), text="Course", bd=6)
        self.lblCourse.grid(row=0, column=0, sticky=W)


        self.cboCourse = ttk.Combobox(CourseFrame, font=('arial', 12, 'bold'),\
            width=51, textvariable=self.Course, state="readonly")
        self.cboCourse['value'] = ('','BSc Serious Game','BCs Computer Science','BA Animation',\
            'BSc Information System', 'BSc Computing', 'BSc Computer Game', 'BSc Computer Animation')
        self.cboCourse.grid(row=0, column=1)
        self.cboCourse.bind("<<ComboboxSelected>>", CourseData)
        

        self.lblCourseCode = Label(CourseFrame, font=("arial", 12, 'bold'), text='Couse Code', bd=5)
        self.lblCourseCode.grid(row=1, column=0, sticky=W, padx=5)
        self.txtCourseCode = Entry(CourseFrame, font=('arial', 12, 'bold'),\
            bd=5, width=52, textvariable=self.CourseCode)
        self.txtCourseCode.grid(row=1, column=1)

        self.lblFaculty = Label(CourseFrame, font=('arial', 12, 'bold'), text='Faculty Name', bd=6)
        self.lblFaculty.grid(row=2, column=0, sticky=W)
        self.txtFaculty = Entry(CourseFrame, font=('arial', 12, 'bold'),\
            bd=5, width=52, justify='left', textvariable=self.Faculty)
        self.txtFaculty.grid(row=2, column=1)

        self.lblDean = Label(CourseFrame, font=('arial', 12, 'bold'), text='Dean of Faculty', bd=6)
        self.lblDean.grid(row=3, column=0, sticky=W)
        self.txtDean = Entry(CourseFrame, font=('arial', 12, 'bold'),\
            bd=5, width=52, justify='left', textvariable=self.Dean)
        self.txtDean.grid(row=3, column=1)

        self.lblHos = Label(CourseFrame, font=('arial', 12, 'bold'), text='Head of School', bd=6)
        self.lblHos.grid(row=4, column=0)
        self.txtHos = Entry(CourseFrame, font=('arial', 12, 'bold'),\
            bd=5, width=52, justify='left', textvariable=self.Head_of_School)
        self.txtHos.grid(row=4, column=1)

        self.lblProgramLeader = Label(CourseFrame, font=('arial', 12, 'bold'), text='Program Leader', bd=6)
        self.lblProgramLeader.grid(row=5, column=0)
        self.txtProgramLeader = Entry(CourseFrame, font=('arial', 12, 'bold'),\
            bd=5, width=52, justify='left', textvariable=self.ProgramLeader)
        self.txtProgramLeader.grid(row=5, column=1)

        self.lblCourseTutor = Label(CourseFrame, font=('arial', 12, 'bold'), text='Program Leader', bd=6)
        self.lblCourseTutor.grid(row=6, column=0)
        self.txtCourseTutor = Entry(CourseFrame, font=('arial', 12, 'bold'),\
            bd=5, width=52, justify='left', textvariable=self.CourseTutor)
        self.txtCourseTutor.grid(row=6, column=1)

        self.lblBuilding = Label(CourseFrame, font=('arial', 12, 'bold'), text='Building', bd=6)
        self.lblBuilding.grid(row=7, column=0)
        self.txtBuilding = Entry(CourseFrame, font=('arial', 12, 'bold'),\
            bd=5, width=52, justify='left', textvariable=self.Building)
        self.txtBuilding.grid(row=7, column=1)

        #==============StudentStatusFrame======================================
        self.lblHomeStudent = Label(StudentStatusFrame, font=('arial', 12, 'bold'),\
            text="Home Student", bd=10)
        self.lblHomeStudent.grid(row=0, column=0, sticky=W)
        self.cboHomeStudent = ttk.Combobox(StudentStatusFrame, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.HomeStudent, state="readonly")
        self.cboHomeStudent['values'] = ('No','Yes')
        self.cboHomeStudent.current(0)
        self.cboHomeStudent.grid(row=0, column=1)
        
        self.lblOversea = Label(StudentStatusFrame, font=('arial', 12, 'bold'),\
            text="Oversea", bd=10)
        self.lblOversea.grid(row=1, column=0, sticky=W)
        self.cboOversea = ttk.Combobox(StudentStatusFrame, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Oversea, state="readonly")
        self.cboOversea['values'] = ('No','Yes')
        self.cboOversea.current(0)
        self.cboOversea.grid(row=1, column=1)

        self.lblAccommodation = Label(StudentStatusFrame, font=('arial', 12, 'bold'),\
            text="Accommodation", bd=10)
        self.lblAccommodation.grid(row=2, column=0, sticky=W)
        self.cboAccommodation = ttk.Combobox(StudentStatusFrame, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Accommodation, state="readonly")
        self.cboAccommodation['values'] = ('No','Yes')
        self.cboAccommodation.current(0)
        self.cboAccommodation.grid(row=2, column=1)

        self.lblExchangeProg = Label(StudentStatusFrame, font=('arial', 12, 'bold'),\
            text="Exchange Prog", bd=10)
        self.lblExchangeProg.grid(row=3, column=0, sticky=W)
        self.cboExchangeProg = ttk.Combobox(StudentStatusFrame, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Accommodation, state="readonly")
        self.cboExchangeProg['values'] = ('No','Yes')
        self.cboExchangeProg.current(0)
        self.cboExchangeProg.grid(row=3, column=1)

        self.lblScholarship = Label(StudentStatusFrame, font=('arial', 12, 'bold'),\
            text="Scholarship", bd=10)
        self.lblScholarship.grid(row=4, column=0, sticky=W)
        self.cboScholarship = ttk.Combobox(StudentStatusFrame, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Scholarship, state="readonly")
        self.cboScholarship['values'] = ('No','Yes')
        self.cboScholarship.current(0)
        self.cboScholarship.grid(row=4, column=1)

        #=======================================Degree Frame==========
        self.lblBA = Label(DegreeFrame, font = ('arial', 12, 'bold'), text="Bachelor of Art", bd=10)
        self.lblBA.grid(row=0, column=0, sticky=W)
        self.SpBA = Spinbox(DegreeFrame, from_=0, to=20, width=9, font=('arial',14,'bold'),\
            textvariable=self.BA)
        self.SpBA.grid(row=0, column=1, pady=0)

        self.lblBSc = Label(DegreeFrame, font = ('arial', 12, 'bold'), text="Bachelor of Science", bd=10)
        self.lblBSc.grid(row=1, column=0, sticky=W)
        self.SpBSc = Spinbox(DegreeFrame, from_=0, to=20, width=9, font=('arial',14,'bold'),\
            textvariable=self.BSc)
        self.SpBSc.grid(row=1, column=1, pady=0)

        self.lblMA = Label(DegreeFrame, font = ('arial', 12, 'bold'), text="Master of Art", bd=10, anchor='e')
        self.lblMA.grid(row=2, column=0, sticky=W)
        self.SpMA = Spinbox(DegreeFrame, from_=0, to=20, width=9, font=('arial',14,'bold'),\
            textvariable=self.MA)
        self.SpMA.grid(row=2, column=1, pady=0)

        self.lblMSc = Label(DegreeFrame, font = ('arial', 12, 'bold'), text="Master of Science", bd=10)
        self.lblMSc.grid(row=3, column=0, sticky=W)
        self.SpMSc = Spinbox(DegreeFrame, from_=0, to=20, width=9, font=('arial',14,'bold'),\
            textvariable=self.MSc)
        self.SpMSc.grid(row=3, column=1, pady=0)

        self.lblPhD = Label(DegreeFrame, font = ('arial', 12, 'bold'), text="Doctor of Philosophy", bd=10)
        self.lblPhD.grid(row=4, column=0, sticky=W)
        self.SpPhD = Spinbox(DegreeFrame, from_=0, to=20, width=9, font=('arial',14,'bold'),\
            textvariable=self.PhD)
        self.SpPhD.grid(row=4, column=1, pady=0)
        #=========================calendar================================
        def getSelectDate():
            nowDate = cal.get_date()
            self.ResultDate.set(nowDate)
            AddModulescore()
        cal = Calendar(CalendarFrame, selectmode='day', date_pattern='dd-mm-yyyy',\
            font=('arial', 10, 'bold'))
        cal.grid(row=0, column=0)

        #==================================UnitNo========================
        self.lblNo=Label(UnitNo, font=('arial', 12, 'bold'), text='No', padx=0, pady=4)
        self.lblNo.grid(row=0, column=0, sticky=W)
        self.lbl1=Label(UnitNo, font=('arial', 12, 'bold'), text='1', padx=0, pady=4)
        self.lbl1.grid(row=1, column=0, sticky=W)
        self.lbl2=Label(UnitNo, font=('arial', 12, 'bold'), text='2', padx=0, pady=4)
        self.lbl2.grid(row=2, column=0, sticky=W)
        self.lbl3=Label(UnitNo, font=('arial', 12, 'bold'), text='3', padx=0, pady=4)
        self.lbl3.grid(row=3, column=0, sticky=W)
        self.lbl4=Label(UnitNo, font=('arial', 12, 'bold'), text='4', padx=0, pady=4)
        self.lbl4.grid(row=4, column=0, sticky=W)
        self.lbl5=Label(UnitNo, font=('arial', 12, 'bold'), text='5', padx=0, pady=4)
        self.lbl5.grid(row=5, column=0, sticky=W)
        self.lbl6=Label(UnitNo, font=('arial', 12, 'bold'), text='6', padx=0, pady=4)
        self.lbl6.grid(row=6, column=0, sticky=W)
        self.lbl7=Label(UnitNo, font=('arial', 12, 'bold'), text='7', padx=0, pady=4)
        self.lbl7.grid(row=7, column=0, sticky=W)
        self.lbl8=Label(UnitNo, font=('arial', 12, 'bold'), text='8', padx=0, pady=4)
        self.lbl8.grid(row=8, column=0, sticky=W)
        #====================Unit Subject==========================================
        self.lblSelectUnit = Label(UnitSubject, font=('arial', 12, 'bold'), text='Select the subject')
        self.lblSelectUnit.grid(row=0, column=0, sticky=W)

        self.cboSubject1 = ttk.Combobox(UnitSubject, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Subject1, state="readonly")
        self.cboSubject1['values'] = ('','Event Driven Prog')
        self.cboSubject1.current(0)
        self.cboSubject1.grid(row=1, column=0, padx=0, pady=4)
        self.cboSubject1.bind("<<ComboboxSelected>>", setSubject)

        self.cboSubject2 = ttk.Combobox(UnitSubject, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Subject2, state="readonly")
        self.cboSubject2['values'] = ('','Object Oriented', 'Spreadsheet')
        self.cboSubject2.current(0)
        self.cboSubject2.grid(row=2, column=0, padx=0, pady=4)
        self.cboSubject2.bind("<<ComboboxSelected>>", setSubject)

        self.cboSubject3 = ttk.Combobox(UnitSubject, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Subject3, state="readonly")
        self.cboSubject3['values'] = ('','System Analysis', 'Inform Technology')
        self.cboSubject3.current(0)
        self.cboSubject3.grid(row=3, column=0, padx=0, pady=4)
        self.cboSubject3.bind("<<ComboboxSelected>>", setSubject)

        self.cboSubject4 = ttk.Combobox(UnitSubject, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Subject4, state="readonly")
        self.cboSubject4['values'] = ('','Digital Graphics', 'English')
        self.cboSubject4.current(0)
        self.cboSubject4.grid(row=4, column=0, padx=0, pady=4)
        self.cboSubject4.bind("<<ComboboxSelected>>", setSubject)

        self.cboSubject5 = ttk.Combobox(UnitSubject, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Subject5, state="readonly")
        self.cboSubject5['values'] = ('','Games', 'Animation')
        self.cboSubject5.current(0)
        self.cboSubject5.grid(row=5, column=0, padx=0, pady=4)
        self.cboSubject5.bind("<<ComboboxSelected>>", setSubject)

        self.cboSubject6 = ttk.Combobox(UnitSubject, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Subject6, state="readonly")
        self.cboSubject6['values'] = ('','Database', 'Maths')
        self.cboSubject6.current(0)
        self.cboSubject6.grid(row=6, column=0, padx=0, pady=4)
        self.cboSubject6.bind("<<ComboboxSelected>>", setSubject)

        self.cboSubject7 = ttk.Combobox(UnitSubject, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Subject7, state="readonly")
        self.cboSubject7['values'] = ('','AddMaths', 'Physics')
        self.cboSubject7.current(0)
        self.cboSubject7.grid(row=7, column=0, padx=0, pady=4)
        self.cboSubject7.bind("<<ComboboxSelected>>", setSubject)

        self.cboSubject8 = ttk.Combobox(UnitSubject, font=('arial', 12, 'bold'),\
            width=14, textvariable=self.Subject8, state="readonly")
        self.cboSubject8['values'] = ('','Data Science')
        self.cboSubject8.current(0)
        self.cboSubject8.grid(row=8, column=0, padx=0, pady=4)
        self.cboSubject8.bind("<<ComboboxSelected>>", setSubject)
        #================================Unit Score================================
        self.lblSUnit = Label(UnitScore, font=('arial', 12, 'bold'), text='Score')
        self.lblSUnit.grid(row=0, column=0, sticky=W)

        self.txt1 = Entry(UnitScore, font=('airial', 12, 'bold'), width=5,\
            textvariable=self.Module1, state=DISABLED)
        self.txt1.grid(row=1, column=0, padx=0, pady=3)
        self.txt2 = Entry(UnitScore, font=('airial', 12, 'bold'), width=5,\
            textvariable=self.Module2, state=DISABLED)
        self.txt2.grid(row=2, column=0, padx=0, pady=3)
        self.txt3 = Entry(UnitScore, font=('airial', 12, 'bold'), width=5,\
            textvariable=self.Module3, state=DISABLED)
        self.txt3.grid(row=3, column=0, padx=0, pady=3)
        self.txt4 = Entry(UnitScore, font=('airial', 12, 'bold'), width=5,\
            textvariable=self.Module4, state=DISABLED)
        self.txt4.grid(row=4, column=0, padx=0, pady=3)
        self.txt5 = Entry(UnitScore, font=('airial', 12, 'bold'), width=5,\
            textvariable=self.Module5, state=DISABLED)
        self.txt5.grid(row=5, column=0, padx=0, pady=3)
        self.txt6 = Entry(UnitScore, font=('airial', 12, 'bold'), width=5,\
            textvariable=self.Module6, state=DISABLED)
        self.txt6.grid(row=6, column=0, padx=0, pady=3)
        self.txt7 = Entry(UnitScore, font=('airial', 12, 'bold'), width=5,\
            textvariable=self.Module7, state=DISABLED)
        self.txt7.grid(row=7, column=0, padx=0, pady=3)
        self.txt8 = Entry(UnitScore, font=('airial', 12, 'bold'), width=5,\
            textvariable=self.Module8, state=DISABLED)
        self.txt8.grid(row=8, column=0, padx=0, pady=3)
        #========================================TotalScore===========================
        self.lblTotalScore = Label(ResultFrameLeft, font=('arial',12,'bold'), text='Total Score')
        self.lblTotalScore.grid(row=0, column=0, sticky=W, padx=1)
        self.txtTotalScore = Entry(ResultFrameRight, font=('arial',12),\
            width=15, textvariable=self.TotalScore)
        self.txtTotalScore.grid(row=0, column=0)

        self.lblRanking = Label(ResultFrameLeft, font=('arial',12,'bold'), text='Ranking')
        self.lblRanking.grid(row=1, column=0, sticky=W, padx=1)
        self.txtRanking = Entry(ResultFrameRight, font=('arial',12,'bold'),\
            width=15, textvariable=self.Ranking)
        self.txtRanking.grid(row=1, column=0)

        self.lblDateRanked = Label(ResultFrameLeft, font=('arial',12,'bold'), text='Date')
        self.lblDateRanked.grid(row=2, column=0, sticky=W, padx=1)
        self.txtDateRanked = Entry(ResultFrameRight, font=('arial',12,'bold'),\
            width=15, textvariable=self.ResultDate)
        self.txtDateRanked.grid(row=2, column=0)
        #=========================subject============================
        self.lblDataScience = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,
        text='Data Science')
        self.lblDataScience.grid(row=0, column=0, sticky=W)
        self.cboDataScience = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.DataScience, state="readonly")
        self.cboDataScience['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboDataScience.current(0)
        self.cboDataScience.grid(row=0, column=1)

        self.lblEventDrivenPro = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='Event Driven Prog')
        self.lblEventDrivenPro.grid(row=1, column=0, sticky=W)
        self.cboEventDrivenPro = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.EventDrivenPro, state="readonly")
        self.cboEventDrivenPro['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboEventDrivenPro.current(0)
        self.cboEventDrivenPro.grid(row=1, column=1)

        self.lblObjectOriented = Label(TopFrame12b, font=('arial', 12, 'bold'),bd=7,\
            text='Object Oriented')
        self.lblObjectOriented.grid(row=2, column=0, sticky=W)
        self.cboObjectOriented = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.ObjectOriented, state="readonly")
        self.cboObjectOriented['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboObjectOriented.current(0)
        self.cboObjectOriented.grid(row=2, column=1)

        self.lblSpreadSheet = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='SpreadSheet')
        self.lblSpreadSheet.grid(row=3, column=0, sticky=W)
        self.cboSpreadSheet = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.Spreadsheet, state="readonly")
        self.cboSpreadSheet['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboSpreadSheet.current(0)
        self.cboSpreadSheet.grid(row=3, column=1)
        
        self.lblSystemAnalysis = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='System Analysis')
        self.lblSystemAnalysis.grid(row=4, column=0, sticky=W)
        self.cboSystemAnalysis = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.SystemAnalysis, state="readonly")
        self.cboSystemAnalysis['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboSystemAnalysis.current(0)
        self.cboSystemAnalysis.grid(row=4, column=1)

        self.lblInformTechnology = Label(TopFrame12b, font=('arial', 12, 'bold'),bd=7,\
            text='Inform Technology')
        self.lblInformTechnology.grid(row=5, column=0, sticky=W)
        self.cboInformTechnology = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.InformTechnology, state="readonly")
        self.cboInformTechnology['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboInformTechnology.current(0)
        self.cboInformTechnology.grid(row=5, column=1)

        self.lblDigitalGraphics = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='Digital Graphics')
        self.lblDigitalGraphics.grid(row=6, column=0, sticky=W)
        self.cboDigitalGraphics = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.DigitalGraphics, state="readonly")
        self.cboDigitalGraphics['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboDigitalGraphics.current(0)
        self.cboDigitalGraphics.grid(row=6, column=1)

        self.lblEnglish = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='English')
        self.lblEnglish.grid(row=7, column=0, sticky=W)
        self.cboEnglish = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.English, state="readonly")
        self.cboEnglish['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboEnglish.current(0)
        self.cboEnglish.grid(row=7, column=1)

        self.lblGames = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='Games')
        self.lblGames.grid(row=8, column=0, sticky=W)
        self.cboGames = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.Games, state="readonly")
        self.cboGames['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboGames.current(0)
        self.cboGames.grid(row=8, column=1)

        self.lblAnimation = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='Animation')
        self.lblAnimation.grid(row=9, column=0, sticky=W)
        self.cboAnimation = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.Animation, state="readonly")
        self.cboAnimation['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboAnimation.current(0)
        self.cboAnimation.grid(row=9, column=1)

        self.lblDatabase = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='Database')
        self.lblDatabase.grid(row=10, column=0, sticky=W)
        self.cboDatabase = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.Database, state="readonly")
        self.cboDatabase['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboDatabase.current(0)
        self.cboDatabase.grid(row=10, column=1)

        self.lblMaths = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='Maths')
        self.lblMaths.grid(row=11, column=0, sticky=W)
        self.cboMaths = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.Maths, state="readonly")
        self.cboMaths['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboMaths.current(0)
        self.cboMaths.grid(row=11, column=1)

        self.lblAddMaths = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='AddMaths')
        self.lblAddMaths.grid(row=12, column=0, sticky=W)
        self.cboAddMaths = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.AddMaths, state="readonly")
        self.cboAddMaths['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboAddMaths.current(0)
        self.cboAddMaths.grid(row=12, column=1)

        self.lblPhysics = Label(TopFrame12b, font=('arial', 12, 'bold'), bd=7,\
            text='Physics')
        self.lblPhysics.grid(row=13, column=0, sticky=W)
        self.cboPhysics = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'),\
            width=19, textvariable=self.Physics, state="readonly")
        self.cboPhysics['values'] = ('No','Core Unit','Yes', 'Complete')
        self.cboPhysics.current(0)
        self.cboPhysics.grid(row=13, column=1)
        #============================tab2, title=====================
        self.lblTitle = Label(TopFrame11, font=('airial', 40, 'bold'), bd=5, justify=CENTER,\
            text = "Student Details Management System")
        self.lblTitle.grid(padx=180)
        #=============================================================
        scroll_x=Scrollbar(TopFrame12a, orient=HORIZONTAL)
        scroll_y=Scrollbar(TopFrame12a, orient=VERTICAL)

        self.Student_Record = ttk.Treeview(TopFrame12a, height=22,\
            columns=('studentid', "firstname",'address','postcode','gender','dob','mobile','email','parent'),\
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.Student_Record.heading('studentid', text="Student ID")
        self.Student_Record.heading('firstname', text="Firstname")
        self.Student_Record.heading('address', text="Address")
        self.Student_Record.heading('postcode', text="Post Code")
        self.Student_Record.heading('gender', text="Gender")
        self.Student_Record.heading('dob', text="DOB")
        self.Student_Record.heading('mobile', text="Mobile")
        self.Student_Record.heading('email', text="Email")
        self.Student_Record.heading('parent', text="Parent/Guidance")

        self.Student_Record['show']='headings'

        self.Student_Record.column('studentid', width=70)
        self.Student_Record.column('firstname', width=90)
        self.Student_Record.column('address', width=90)
        self.Student_Record.column('postcode', width=200)
        self.Student_Record.column('gender', width=70)
        self.Student_Record.column('dob', width=70)
        self.Student_Record.column('mobile', width=70)
        self.Student_Record.column('email', width=90)
        self.Student_Record.column('parent', width=70)

        self.Student_Record.pack(fill=BOTH, expand=1)


        #====================================buttons on button frame========================
        self.btnAddNewStudent = Button(ButtonFrame, pady=1, padx=15, bd=4, font=('arial', 16, 'bold'),\
            bg='cadetblue', width=5, text='AddNew')
        self.btnAddNewStudent.grid(row=0, column=0, padx=1)
        
        self.btnUpdate = Button(ButtonFrame, pady=1, padx=15, bd=4, font=('arial', 16, 'bold'),\
            bg='cadetblue', width=5, text='Update')
        self.btnUpdate.grid(row=0, column=1, padx=1)
        
        self.btnDelete = Button(ButtonFrame, pady=1, padx=15, bd=4, font=('arial', 16, 'bold'),\
            bg='cadetblue', width=5, text='Delete')
        self.btnDelete.grid(row=0, column=2, padx=1)
        
        self.btnReset = Button(ButtonFrame, pady=1, padx=15, bd=4, font=('arial', 16, 'bold'),\
            bg='cadetblue', width=5, text='Reset', command=Reset)
        self.btnReset.grid(row=0, column=3, padx=1)

        self.btnResult = Button(ButtonFrame, pady=1, padx=15, bd=4, font=('arial', 16, 'bold'),\
            bg='cadetblue', width=5, text='Result', command = getSelectDate)
        self.btnResult.grid(row=0, column=4, padx=1)
        
        self.btnExit = Button(ButtonFrame, pady=1, padx=15, bd=4, font=('arial', 16, 'bold'),\
            bg='cadetblue', width=5, text='Exit', command=iExit)
        self.btnExit.grid(row=0, column=5, padx=1)
        





if __name__ == '__main__':
    main()