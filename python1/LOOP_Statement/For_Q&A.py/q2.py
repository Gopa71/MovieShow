# 2: Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
n=0
n1=0
ls=[1,2,3,4,5,6,7,8,9,10,11]
for i in ls:
    if i%2==0:
        n+=1
    else:
        n1+=1
print("Number of even number :",n)
print("Number of odd number :",n1)