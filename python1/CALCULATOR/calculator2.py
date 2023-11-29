from tkinter import *

root=Tk()
root.title("CALCULATOR")
e=Entry(root)
e.grid(row=0,columnspan=6,sticky=W+E)

i=0
def get_variable(n):
      global i
      e.insert(i,n)
      i+=1
def clear_all():
      e.delete(0,END)
def undo():
      a=e.get()
      if len(a):
            ls=a[:-1]
            clear_all()
            e.insert(0,ls)
      else:
            clear_all()
            e.insert(0,"error")
def operator(op):
      global i
      l=len(op)
      e.insert(i,op)
      i+=l
def calculat():
      s=e.get()
      try:
         a=eval(s)
         clear_all()
         e.insert(0,a)
      except:
            clear_all()
            print("Error")
Button(root,text="1",command=lambda:get_variable(1)).grid(row=1,column=0)
Button(root,text="2",command=lambda:get_variable(2)).grid(row=1,column=1)
Button(root,text="3",command=lambda:get_variable(3)).grid(row=1,column=2)
Button(root,text="4",command=lambda:get_variable(4)).grid(row=2,column=0)
Button(root,text="5",command=lambda:get_variable(5)).grid(row=2,column=1)
Button(root,text="6",command=lambda:get_variable(6)).grid(row=2,column=2)
Button(root,text="7",command=lambda:get_variable(7)).grid(row=3,column=0)
Button(root,text="8",command=lambda:get_variable(8)).grid(row=3,column=1)
Button(root,text="9",command=lambda:get_variable(9)).grid(row=3,column=2)
Button(root,text="0",command=lambda:get_variable(0)).grid(row=4,column=0)
Button(root,text="AC",command=lambda:clear_all()).grid(row=4,column=1)
Button(root,text="<-",command=lambda:undo()).grid(row=1,column=3)

Button(root,text="/",command=lambda:operator('/')).grid(row=1,column=4)
Button(root,text=")",command=lambda:operator(')')).grid(row=1,column=5)
Button(root,text="+",command=lambda:operator('+')).grid(row=2,column=3)
Button(root,text="π",command=lambda:operator('3.14')).grid(row=2,column=4)
Button(root,text="exp",command=lambda:operator('**')).grid(row=2,column=5)
Button(root,text="-",command=lambda:operator('-')).grid(row=3,column=3)
Button(root,text="%",command=lambda:operator('%')).grid(row=3,column=4)
Button(root,text="x!").grid(row=3,column=5)
Button(root,text="=",command=lambda:calculat()).grid(row=4,column=2)
Button(root,text="*",command=lambda:operator('*')).grid(row=4,column=3)
Button(root,text="(",command=lambda:operator('(')).grid(row=4,column=4)
Button(root,text="^2",command=lambda:operator('**2')).grid(row=4,column=5)
root.mainloop()