# 6:Create a program that prints a diamond shape using nested for loops. You can specify the number of rows for the diamond. For example, for n = 5, the diamond would look like this:
# Create a program that prints a diamond shape using nested for loops. You can specify the number of rows for the diamond. For example, for n = 5, the diamond would look like this:

#   *
#  * *
# * * *
#  * *
#   *
n=3
for i in range(n):
    for j in range(i,n):
        print(" ",end="")      
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(1,i+1):
        print(" ",end="")      
    for j in range(i,n):
        print("*",end=" ")
    print()    
