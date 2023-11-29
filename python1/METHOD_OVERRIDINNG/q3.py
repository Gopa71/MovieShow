# Question 2: Create a base class called Animal. Define a method in the Animal class called speak() that returns "Animal speaks." Create two subclasses, Dog and Cat. Override the speak() method in both subclasses to provide a unique implementation for each. Create instances of both Dog and Cat and call their speak() methods to hear what they say.
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog can speaks")
class Cat(Animal):
    def speak(self):
        print("Cat can speaks")
x=Dog()
x.speak()
x=Cat()
x.speak()
