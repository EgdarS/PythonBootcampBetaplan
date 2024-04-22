from bankAccount import bankAccount
class User:
    type = 'human'
    def __init__(self, firstName='Default', lastName='User', email='test@test.com', amount=0, pin='1234'):
        self.email=email
        self.bankAccount=bankAccount(accountHolder=email, pin=pin)

    def getFirstName(self):
        print(f'Your name is {self.firstName}')
        return self
    def getLastName(self):
        print(f'Your last name is {self.lastName}')
        return self
    def getEmail(self):
        print(f'Your email is{self.email}')
        return self
    

egi=User('Egdar', 'Shaqiri', 'egi.shaqiri99@gmail.com', pin='1234')

#egi.bankAccount.deposit(input('Enter pin: '), input('How much do you want to deposit? '))
#egi.bankAccount.showAmount(input('Enter pin: '))
#egi.bankAccount.withdraw(input('Enter pin: '), input('How much do you want to withdraw? '))
#egi.bankAccount.interestRate(input('Enter pin:'), input('Enter interest rate:'))