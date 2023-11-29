i=int(input("Enter the binary code "))
n=int(input("Enter the count of binary code"))
decimal=i*(2**(n-1-i))
print("The decimal of",i,"is",decimal)
