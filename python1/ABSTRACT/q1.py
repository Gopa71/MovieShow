# Question: Implement a class Employee with private attributes name, salary, and id. Add methods to increase the salary and display employee information.
class Employee:
    def __init__(self,name,salary,id):
        self.__name=name
        self.__salary=salary
        self.__id=id
    def Salary(self,amount):
        self.__salary+=amount
    def Details(self):
        return  self.__name,self.__id
x=Employee()
