# Write a program that checks if a given year is leap year.A leap year is divisible by 100 but not divisible by 400.Print "Leap Yera "or "Not a leap year"
a=int(input("Enter a year For checking is leap year or not :"))
if a%4==0:
    if a%100==0:
       print(a,"is leap year")
    else:
        print(a,"is not leap year")
else:
    print(a,"is not leap year")