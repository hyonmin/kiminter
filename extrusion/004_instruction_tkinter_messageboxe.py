from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('messagebox')


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    messagebox.showerror("careful")

# popup of askyesno and askokcancel
# a variable 'response' is assigned as a string type if you choose 'yes', the value would be '1'
# if you choose 'no', the value would be '0'.
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ popup of askquestion if you choose 'yes' returns 'yes'
# as a string value. if you choose 'no' it returns 'no' as a string value. 

def yesno():
    response = messagebox.askyesno("yes of no")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="YES?").pack()
    else:
        Label(root, text='no?').pack()

# I tested an app made by myself. there was a popup window to make users choose options.
# making a wrong choice, users have a warning message. but there was a problem that the
# warning popup was shown behind the option popup window.
# This is the thing you can deal with it.
# withdraw() and deiconify()
# first, that withdraws the popup window of options so that the warning message popup
# can be shown uppermost.
# second, after the warning popup is removed, the options' popup is given back.
"""
root.withdraw()
messagebox.showwarning('blah, blah~')
root.deiconify()
"""





Button(root, text = "popup", command = popup).pack()
Button(root, text = "yesno", command = yesno).pack()

mainloop()