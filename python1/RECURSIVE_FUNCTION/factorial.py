
def add(a):
    if a==0:
        return 1
    else:
      return  a * add(a-1)
print(add(5))