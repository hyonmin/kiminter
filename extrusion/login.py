import tkinter.ttk as ttk
from tkinter import *
from datetime import datetime, timedelta

class Access(Tk):
    # create a window
    def __init__(self):
        super().__init__()
        self.title("Access")
        self.geometry("250x400+800+300")
        self.resizable(0,0)

        #configure the grid
        for i in range(4):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)

        self.create_widgets()
    
    # create a combobox containing dates
    def create_widgets(self):
        def choice(self, group):
            if combo_date.get() in dates:
                a = (combo_date.get(),group)
                self.destroy()

            else:
                self.withdraw()
                from tkinter import messagebox
                messagebox.showerror("Error", "Choisirez bien la date.")
                self.deiconify()

        dates = [(datetime.today() - timedelta(days=i)).strftime('%d-%b-%Y') for i in range(2)]

        combo_date = ttk.Combobox(self, height = 5, values=dates,\
            font=('calibre', 15, 'bold'),state = "readonly")
        combo_date.set("Date de travail")


        btn1 = Button(self, text = "Equipe A", font=('calibre', 15, 'bold'),\
              height=2, width=8, bd=3, command = lambda: choice(self, "A"))

        btn2 = Button(self, text = "Equipe B", font=('calibre', 15, 'bold'),\
              height=2, width=8, bd=3, command = lambda: choice(self, "B"))

        btn3 = Button(self, text = "Equipe C", font=('calibre', 15, 'bold'),\
              height=2, width=8, bd=3, command = lambda: choice(self, "C"))

        combo_date.grid(row=0, column=0)
        btn1.grid(row=1, column = 0)
        btn2.grid(row=2, column = 0)
        btn3.grid(row=3, column = 0)




if __name__ == "__main__":
    login = Access()
    login.mainloop()



"""
paper1 = Tk()
paper1.title("Login Extrusion Manager")
paper1.geometry("460x320+700+300") #1920*1080
paper1.resizable(False, False)

label1 = Label(paper1, text="Présentez-vous", font = ('calibre', 15, 'bold')).place(x=155, y=5)
label2 = Label(paper1, text="Kim International", font = ('calibre', 15, 'bold')).place(x=155, y=285)

label_name = Label(paper1, text = "Nom", font = ('calibre', 13, 'normal')).place(x=40, y=60)
label_password = Label(paper1, text = "Mot de passe", font = ('calibre', 13, 'normal')).place(x=40, y=100)


name = StringVar()
password = StringVar()
entry_name_input_area = Entry(paper1, textvariable = name, width = 20, \
                              font = ('calibre', 13, 'normal')).place(x=180, y=60)

entry_password_input_area = Entry(paper1, textvariable = password, width = 20, \
                                  show = '*', font = ('calibre', 13, 'normal')).place(x=180, y=100)

btn1 = Button(paper1, padx=10, pady=7, text="Présenter", bd=3).place(x=188, y=148)

paper1.mainloop()
"""