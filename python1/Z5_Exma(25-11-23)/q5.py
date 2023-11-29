# 5.Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz." For numbers that are multiples of both three and five, print "FizzBuzz."?.(10)
for i in range(1,101):  
    if i%3==0 and i%5==0:
        print("fizzBuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
          print('fizz')
    else:
         print(i)