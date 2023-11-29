# 5:If your programming language supports if statements, create a program that takes a day of the week as input (e.g., "Monday", "Tuesday") and provides a message based on the day (e.g., "It's a workday." or "It's the weekend.")
a=str(input("Enter the day : "))
if a=="Monday" or a=="tuesday" or a=="wednesday" or a=="thusday" or a=="friday" or a=="saturday":
        print("It's a workday.")
else:
        print("It's the weekend.")