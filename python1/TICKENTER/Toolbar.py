from tkinter import *
root=Tk()
def click():
    print("Mouse clicked")

mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)
mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New file",command=click)
submenu.add_command(label="New text file",command=click)
submenu.add_command(label="New window")
submenu.add_separator()
submenu.add_command(label="New file")
submenu.add_command(label="New text file")
submenu.add_command(label="New window")

newsubmenu=Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newsubmenu)
newsubmenu.add_command(label="undo")
newsubmenu.add_command(label="Reundo")
newsubmenu.add_separator()
newsubmenu.add_command(label="find")
newsubmenu.add_command(label="replace")

toolbar=Frame(root,bg="purple")
Button(toolbar,text="crop").pack(side=LEFT,padx=10,pady=10)
toolbar.pack(side=TOP,fill=X)




root.mainloop()
