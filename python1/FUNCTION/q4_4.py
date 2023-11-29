# 4. Write a function find_max that takes a list of numbers as an argument and returns the largest number in the list
ls=[5,3,6,2,7,8,3,4]
n=0
def find_max(n):
   for i in ls:
       if i>n:
         n=i
         return n
print(find_max(n))

   

