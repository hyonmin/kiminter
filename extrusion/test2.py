
'''
from datetime import datetime, timedelta

dates = [(datetime.today() - timedelta(days=i)).strftime('%d-%m-%Y') for i in range(5)]

print(datetime.today() - timedelta(days=1))
print(dates)
'''
from tkinter import *

def main():
    w = Tk()
    k(w)
    w.mainloop()

class k:
    def __init__(self, master):
        self.master = master        
        self.master.geometry('100x100')
        a = True


        Button(self.master, text="click to test", command=self.goto).pack()


        



    def goto(self):
        import report_prod
        report_prod.reports(self, 2, "02/03/2022")

if __name__ == "__main__":
    main()

