from abc import ABC,abstractmethod
class Vehicle(ABC):
    def str_engin(self):
        print("Engin started")
    def breek(self):
        print("apply break")
    def stp_engin(self):
        print("Engin stop")
     
class Car(Vehicle):
    def sunroof(self):
        print("car have sunroof")
class Truck(Vehicle):
    def sunroof(self):
        print("Truck have sunroof")
x=Car()
x.sunroof()