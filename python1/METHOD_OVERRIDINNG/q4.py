# Question 3: Create a base class called Vehicle. Define a method in the Vehicle class called start_engine() that prints "Engine started." Create two subclasses, Car and Motorcycle. Override the start_engine() method in both subclasses to provide different messages. Create instances of both Car and Motorcycle and call their start_engine() methods to see the messages.
class Vehicle:
    def start_engine(self):
       print("Engine started")
class Car(Vehicle):
    def start_engine(self):
       print("Engine started in car")  
class Motorcycle(Vehicle):
    def start_engine(self):
       print("Engine started in motorcycle") 
x=Car()
x.start_engine()
x=Motorcycle()
x.start_engine()
