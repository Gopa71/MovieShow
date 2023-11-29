from tkinter import *
root=Tk()
n=0
def fun():
    for i in range(1,101):
        if i%2==0:
            n=i
            print(n)
Button(root,text="click",command=fun).pack()
root.mainloop()