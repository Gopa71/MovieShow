# 11:Write a program that prompts the user to enter the current month (as a number from 1 to 12) and uses elif statements to determine and print the season (e.g., "Spring," "Summer," "Fall," or "Winter").
a=int(input("Enter Month : "))
if a==1 or a==2 or a==3 or a==4:
    print("It's a spring season")
elif a==5 or a==6 or a==7 or a==8:
    print("It's a summer season")
elif a==9 or a==10 or a==11 or a==12:
    print("it's a winter season ")