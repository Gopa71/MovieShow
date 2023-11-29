ls=[]

while True:
    print("1.add Todo\n2.Display Todo\n3.Delete Todo\n4.Exit")
    a=int(input("Enter your choice : "))
    if a==1:
       txt=str(input("Enter task to add\n"))
       ls.append(txt)
       
    elif a==2:
       print("The tasker are :\n")
       for i in ls:
         print("*",i)
      
    elif a==3:
          remove=str(input("Enter the task for remove : "))
          ls.remove(remove)
    elif a==4:
        break
    


