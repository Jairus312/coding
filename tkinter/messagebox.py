from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert","stop! virus has been found")

Button = Button(root,text = "scan for virus",command = msg)
Button.place(x = 40,y = 80)

root.mainloop()
