while True:
    print("1.Adition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exit")
    x=int(input("Enter your choice : "))
    if x==1:
        a=int(input("Enter first number : "))
        b=int(input("Enter Second number : "))
        add=a+b
        print(a,"+",b,"=",add)
    elif x==2:
        a=int(input("Enter first number : "))
        b=int(input("Enter Second number : "))
        sub=a-b
        print(a,"-",b,"=",sub)
    elif x==3:
        a=int(input("Enter first number : "))
        b=int(input("Enter Second number : "))
        mul=a*b
        print(a,"+",b,"=",mul)
    elif x==4:
        try:
            a=int(input("Enter first number : "))
            b=int(input("Enter Second number : "))
            sum=a/b
            print(a,"/",b,"=",sum)
        except:
            print(a,"/",b,"Is not posible")
    elif x==5:
        break
