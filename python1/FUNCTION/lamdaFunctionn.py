# x= lambda a,b:a+b
# print(x(5,6))
def add(a):
    return lambda b:b+a
x=add(5)
print(x(3))
