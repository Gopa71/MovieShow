from tkinter import *
def add():
    a=float(e1.get())
    b=float(e2.get())
    print(a+b)
root=Tk()
e1=Entry(root)
e1.pack()
e2=Entry(root)
e2.pack()
Button(root,text="click",command=add).pack()
root.mainloop()
  