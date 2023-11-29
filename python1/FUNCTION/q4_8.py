# 8. Create a function count_vowels that takes a string as an argument and returns the number of vowels (a, e, i, o, u) in the string.
ls=list()
n=0
def count_vowels(a):
    for i in ls:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            n+=1
        return n
a=str(input("Enter a string : "))
print(count_vowels(a))
print(n)