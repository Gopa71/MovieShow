import math as m


def qua():
    a=int(input("Enter the first value : "))
    b=int(input("Enter the second value : "))
    c=int(input("Enter the third value : "))
    s1=b**2
    s2=4*a*c
    s3=int(s1-s2)
    s=m.sqrt(s3) 
    print(s)
