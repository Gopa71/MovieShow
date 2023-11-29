
# 6. Define a function reverse_string that takes a string as an argument and returns the string reversed.
ls=list()
def rev(n):
    for i in n:
       ls.append(i)
    ls.reverse()
    return "".join(ls)
n=str(input("Enter a string : "))
print(rev(n))
