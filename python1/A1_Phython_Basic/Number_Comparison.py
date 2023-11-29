# Write a program that takes two numbers as input and determines whether the first number is greater,less than,or equal to the second number.print the appropriate message.
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
if a<b:
    print(a,"Is Lessthan",b)
elif a==b:
    print(a,"IS equalto ",b)
else:
    print(a,"Is greater than ",b)
