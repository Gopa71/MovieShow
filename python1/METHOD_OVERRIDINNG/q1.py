# Question: Create a Python program that demonstrates polymorphism using a base class and two derived classes. The base class should have a method called display_info(), and both derived classes should override this method with their own implementations. Then, create instances of both derived classes and call the display_info() method on each of them to demonstrate polymorphism.
class A:
    def display_info(self):
        print("Enter 1st name")
class B(A):
    def display_info(self):
        print("Enter 2nd name")
    def add3(self):
        print("Enter 3rd name")
        super().display_info()
class C(A):
    def display_info(self):
        print("Enter 4th name")
    def add3(self):
        print("Enter 5th name")
x=B()
x.display_info()
x.add3()
x=C()
x.display_info()
x.add3()

