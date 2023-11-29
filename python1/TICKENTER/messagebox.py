from tkinter import *
from tkinter import messagebox
root=Tk()
def asd():
    messagebox.askretrycancel("Message","Are you sure?")
bt=Button(root,text="Click",command=asd).pack()
root.mainloop()