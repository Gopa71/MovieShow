class BankAccount:
    def _init_(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    def get_balance(self):
        return self.__balance
        print(self.__balance)
    def deposite(self,amount):
        if amount>0:
            self.__balance+= amount
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Invalid withdrawal amount")
x=BankAccount()
x._init_(" ",5000)
x.get_balance()
# x.deposite(3000)
# x.withdraw(9000)
    


