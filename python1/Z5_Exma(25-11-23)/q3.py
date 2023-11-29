# 3.Write a Python function to calculate the factorial of a given number using recursive function?.(10)
s=int(input("Enter a number for finding factorial : "))
def rec(a):
    if a==1:
        return 1
    else:
        return a * rec(a-1)
print(rec(s))