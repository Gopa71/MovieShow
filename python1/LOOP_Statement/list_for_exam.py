# list=[1,2,4,5]
# ls=list.pop()
# print(ls)
''''llllll'''
# n=5
# for i in range(n):
#     for j in range(i+1,n):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="  ")
#     print()
# for i in range(n):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for j in range(i+1,n-1):
#         print("*",end="  ")
#     print()
'''//////'''
# txt="synnefo"
# for i in range(len(txt)):
#     print(txt[:i+1])
'''//////'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
'''//////'''
# n=6
# for i in range (n):
#     for j in range(i,n):
#        print(" ",end="")
#     for j in range(1,i+1):
#        print("*",end="")
#     for j in range(1,i+1):
#        print("*",end="")
#     print()
# for i in range(n):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for j in range(i,n):
#         print("*",end="")
#     for j in range(i,n):
#         print("*",end="")
#     print()
a=int(input("Enter a 3digit number : "))
y=0
x=0
while a>0:
    x=a%10
    y+=x
    a=a//10
print(y)
