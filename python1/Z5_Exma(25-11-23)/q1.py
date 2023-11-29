# 1.Write a Python function to check if a given string is a palindrome?.(10)
ls=list()
def rev(a):
    for i in s:
        ls.append(i)
    ls.reverse()
    return "".join(ls)
s=input("Enter the string :")
d=rev(s)
if s==d:
    print("the string is palindrome")
else:
    print("the string is not palindrome")


