ls=[1,2,3,4,5,5,6,6,7,8,8,8,9,10]
print("The list is ",ls)
print("The duplicate elements are :")
for i in ls:
    if ls.count(i)>=2:
       print(i)
       ls.remove(i)
print(ls)        