class Std:
    def __init__(self,Name,Subject1,Subject2,Subject3):
         self.Name=Name
         self.Subject1=Subject1
         self.Subject2=Subject2
         self.Subject3=Subject3
    def getData(self):
         self.Name=input("Enter the name : ")
         self.Subject1=input("Enter the subject name : ")
         self.mark1=int(input("Enter the subject Mark : "))
         self.Subject2=input("Enter the subject name : ")
         self.mark2=int(input("Enter the subject Mark : "))
         self.Subject3=input("Enter the subject name : ")
         self.mark3=int(input("Enter the subject Mark : "))
    def getDisplay(self):
         self.per=(self.mark1 + self.mark2 + self.mark3)/300*100
         print("The total percenteage of thestudent is :",self.per)
obj=Std(" "," "," "," ")
obj.getData()
obj.getDisplay()       

