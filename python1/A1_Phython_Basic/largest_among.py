"""a=int(input("Enter first Number :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third Number :"))
if a>b and a>c:
    print(a,"is greater")
elif b>c:
    print(b,"is greater")
else:
    print(c,"is greater")"""


# a=int(input("Enter first Number :"))
# b=int(input("Enter Second Number :"))
# c=int(input("Enter Third Number :"))
# if a>b:
#      if a>c:
#           print(a,"is greater")
# elif b>c:
#      print(b,"is greater")
# else:
#      print(c,"is greater")


a=int(input("Enter first Number :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third Number :"))
if a>b:
     if a>c:
          print(a,"is greater")
     else:
          print(c,"is greater")
else:
     if b>c:
          print(b,"is greater")
     else: 
          print(c,"is greater")