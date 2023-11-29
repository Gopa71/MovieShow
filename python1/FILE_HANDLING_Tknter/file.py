from tkinter import *
root=Tk()
display=Entry(root)
display.pack()

file=open("file.txt","a")
def add():
    s=display.get()
    file.write(s)

Button(root,text="add",command=lambda:add()).pack()

root.mainloop()