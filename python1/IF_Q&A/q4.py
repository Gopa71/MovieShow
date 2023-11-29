# 4:Create a program that asks the user for their grade (A, B, C, D, or F). Depending on the grade entered, provide the following feedback:

# A: "Excellent!"
# B: "Good job!"
# C: "Not bad."
# D: "You can do better."
# F: "You need to work harder."
a=str(input("Enter your Grade (A, B, C, D, or F): "))
if a=="A":
    print("Excellent!")
elif a=="B":
    print("Good job!")
elif a=="C":
    print("Not bad.")
elif a=="D":
    print("You can do better")
elif a=="F":
    print("You need to work harder.")