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

    def account_type(self):
        print("normal account")

# account = BankBalance("harsh",500)
# account.deposit(200)
# account.withdraw(200)
# print(account.get_balance())

class StudentBalance(BankBalance):
    def studentBenifit(self):
        print(self.owner,"is a student hence he will get student benfit")

    def account_type(self):
        print("student account")

harsh = StudentBalance("harsh",500)
harsh.studentBenifit()