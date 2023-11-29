from tkinter import *
class Ex:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.b1=Button(frame,text="Click",command=self.cmd)
        self.b1.pack()
        self.b2=Button(frame,text="Exit",command=frame.quit)
        self.b2.pack()
    def cmd(self):
        print("haii")
root=Tk()
obj=Ex(root)
root.mainloop()


