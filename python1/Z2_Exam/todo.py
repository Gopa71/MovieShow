ls=[]
while True:
    print("1.addtodo\n2.displaytodo\n3.deletetodo\n4.exit")
    a=int(input("Enter a Number"))
    if a==1:
        b=int(input("Enter a number to insert"))
        ls.append(b)
    elif a==2:
        print(ls)
    elif a==3:
        b=int(input("Enter a number to remove"))
        ls.remove(b)
    elif a==4:
        break
    # callback,callbackhell,promise