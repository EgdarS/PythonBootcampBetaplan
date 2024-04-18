from bankAccount import BankAccount

class User:
    def  __init__(self, firstName='Default', lastName='user', email='test.email.com', pin='1234'):
        self.firstName= firstName
        self.lastName=lastName
        self.email=email
        self.pin=pin
        self.bankAccount=BankAccount(1.3, 50)

    def getBalance(self):
        self.bankAccount.display_account_info()
        return self


egi=User('Egdar','Shaqiri','egi.shaqiri99@gmail.com',1234)


# egi.bankAccount.display_account_info()
# egi.bankAccount.deposit()
# egi.bankAccount.withdraw()
# egi.bankAccount.yield_interest()

