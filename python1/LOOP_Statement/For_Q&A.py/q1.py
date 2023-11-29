# 1: Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
n=int(input("Enter limit : "))
for i in range(n):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print("\n")
# n=5
# for i in range(n):
#     for j in range():
#         print('*',end=" ")
#     print()
# for i in range(n):
#     for j in range(i-1,n):
#         print('*',end=" ")
#     print()