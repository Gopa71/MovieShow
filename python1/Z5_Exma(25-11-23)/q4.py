# .find duplicate from given array and delete the element then print output element?.(10)
ls=[1,2,3,4,4,5,6]
for i in ls:
    if ls.count(i)>=2:
        print(i)
        ls.remove(i)
print(ls)