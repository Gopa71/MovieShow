# Create a Python program that demonstrates method overriding with a base class and two derived classes. The base class should have a method called calculate_area(), and both derived classes should override this method with their own implementations for calculating the area of different geometric shapes. Then, create instances of both derived classes and call their calculate_area() methods to see the overridden behavior.
class Area:
     def calculate_area(self):
          a=int(input("Enter the height : "))
          b=int(input("Enter the bridth :  "))
          area=(a*b)/2
          print("Area of 1st triange is : ",area )
class A(Area):
     def calculate_area(self):
          a=int(input("Enter the height : "))
          b=int(input("Enter the bridth :  "))
          area=(a*b)/2
          print("A Area of 2nd triange is : ",area )
class B(Area):
     def calculate_area(self):
          a=int(input("Enter the height : "))
          b=int(input("Enter the bridth :  "))
          area=(a*b)/2
          print("B Area of 3rd triange is : ",area )
x=A()
x.calculate_area()
x=B()
x.calculate_area()
