class BankBalance():
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,money):
        self.__balance = self.__balance + money

    def withdraw(self,amount):
        if amount < self.__balance :
           self.__balance = self.__balance-amount

    def get_balance(self):
        return self.__balance

account = BankBalance("harsh",500)
account.deposit(200)
account.withdraw(200)
print(account.get_balance())
