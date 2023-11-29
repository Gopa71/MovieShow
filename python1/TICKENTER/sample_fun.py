from tkinter import *
root=Tk()
def fun():
    print("clicked")
Button(root,text="Click",command=fun).pack()
root.mainloop()
