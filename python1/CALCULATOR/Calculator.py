from tkinter import *
root=Tk()
f1=Frame(root)
f1.pack()
f2=Frame(root)
f2.pack()
e=Entry(f1)
e.pack()


# def one():
#     a=e.get()
#     print(a)
b1=Button(f2,text="1")
# b1.pack()
b2=Button(f2,text="2")

b3=Button(f2,text="3")

b4=Button(f2,text="+")

b5=Button(f2,text="<-")

b6=Button(f2,text="4")

b7=Button(f2,text="5")

b8=Button(f2,text="6")

b8_1=Button(f2,text="-")

b9=Button(f2,text="EE")

b10=Button(f2,text="7")

b11=Button(f2,text="8")

b12=Button(f2,text="9")

b13=Button(f2,text="x")

b14=Button(f2,text="%")

b15=Button(f2,text=".")

b16=Button(f2,text="0")

b17=Button(f2,text="=")

b18=Button(f2,text="/")

b19=Button(f2,text="π")


b1.grid(row=0,column=0)
b2.grid(row=0,column=1)

b3.grid(row=0,column=2)

b4.grid(row=0,column=3)

b5.grid(row=0,column=4)

b6.grid(row=1,column=0)

b7.grid(row=1,column=1)

b8.grid(row=1,column=2)
b8_1.grid(row=1,column=3)

b9.grid(row=1,column=4)

b10.grid(row=2,column=0)

b11.grid(row=2,column=1)

b12.grid(row=2,column=2)

b13.grid(row=2,column=3)

b14.grid(row=2,column=4)

b15.grid(row=3,column=0)

b16.grid(row=3,column=1)

b17.grid(row=3,column=2)

b18.grid(row=3,column=3)

b19.grid(row=3,column=4)




# root.mainloop()
# from tkinter import *

# def display_text():
#     value = button_text.get()
#     result_label.config(text=value)

# # Create the main window
# root = Tk()
# root.title("Button Value Display Example")

# # Create a frame
# frame =Frame(root)
# frame.pack(padx=10, pady=10)

# # Create a Button with a label
# button_text = StringVar()
# button = Button(frame, textvariable=button_text, command=display_text)
# button_text.set("Click me!")
# button.pack()

# # Create a Label to display the value
# result_label = Label(frame, text="")
# result_label.pack()
root.mainloop()
