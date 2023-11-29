# 4: Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
x=0
y=1
print(x,"",end="")
print(y,"",end="")
for i in range(1,9):
    s=x+y
    x=y
    y=s
    print(s,"",end="")
   

