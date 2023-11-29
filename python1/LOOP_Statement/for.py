# for i in range(1,101,1):
#      if i%5==0 and i%3==0:
#         print ("fizzbuzz")
#      elif i%5==0:
#         print("buzz")
#      elif i%3==0:
#         print("fizz")
#      else:
#         print(i)

'''vowel_find'''
# n=0
# a=str(input("Enter a letter :"))
# for i in a:
#     if i=='a' or i=="e" or i=='i' or i=='o' or i=='u':
#        n+=1
# print(n)


'''Multiplication_Table'''
# a=int(input("Enter a Number :"))
# for i in range(1,11,1):
#      n=i*a
#      print(i,"x",a,"=",n)


'''Print first 10even numbers in revers order'''
# n=2
# for i in range(11,1,-1):
#     if i%n==0:
#       print(i)

'''Factorial'''
# a=int(input("Enter the number for finding then factorial :"))
# for i in range(a,1):
#      n=i*a
#      print(n)
#      i+=1

# for i in range(1,6):
#      for j in range(1,i+1):
#           print("*",end=" ")
#      print("\n")

n=6
for i in range(n):
    for j in range(1,n):
        print(j,end=" ")
    n-=1
    print("\n")
