class A:
    def add1(self):
        print("Enter 1st name")
    def add(self):
        print("Enter 2nd name")
class B(A):
    def add3(self):
        print("Enter 3rd name")
    def add(self):
        print("Enter 4th name")
        super().add()
x=B()
x.add1()
x.add()
x.add3()
