# from tkinter import *
# root=Tk()
# e=Entry(root)
# e.pack()
# ls=[]
# labels = []
# buttons = []
# def clr_all():
#      e.delete(0,END)
# def Add():
#      global ls
#      # s=e.get()
#      ls.append(e.get())
#      disp()
#      clr_all()
# def asa():
#     for label in labels:
#         label.destroy()
#     for button in buttons:
#         button.destroy()
# def disp():
#      asa() 
#      for i in ls:
#           Label(root,text=i).pack()
#           Button(root,text="del",command=lambda:dele(i)).pack()
#      # l=Label(root,text="")
#      # l.pack()  #grid(row=1,column=0)
#      # b=Button(root,text="Del",command=lambda:dele(i))
#      # b.pack()  #grid(row=1,column=1)
#      # global ls
#      # for i in ls:
#      #      print(i)
#      #      l.config(text=i)
           
          
# def dele(a):  
#      global ls        
#      print(a)         
#      print(ls)         
#      ls.remove(a)
#      # clr_all()
#      print("af",ls) 
#      disp()  
     
# Button(root,text="Add",command=lambda:Add()).pack()

# root.mainloop()
from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
ls = []
labels = []
buttons = []

def clr_all():
    e.delete(0, END)

def Add():
    global ls
    ls.append(e.get())
    disp()
    clr_all()

def asa():
    for label in labels:
        label.destroy()
    for button in buttons:
        button.destroy()

def disp():
    asa()
    global ls, labels, buttons
    labels = []
    buttons = []
    for i, item in enumerate(ls):
        label = Label(root, text=item)
        label.pack()
        button = Button(root, text="Del", command=lambda i=i: dele(i))
        button.pack()
        labels.append(label)
        buttons.append(button)

def dele(a):
    global ls
    ls.pop(a)
    disp()

Button(root, text="Add", command=Add).pack()

root.mainloop()

    
