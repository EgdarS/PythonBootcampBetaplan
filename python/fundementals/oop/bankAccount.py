class bankAccount:
    def __init__(self, amount=0, accountHolder='Default', pin='1234'):
        self.amount = amount
        self.pin= pin
        self.accountHolder=accountHolder

    def showAmount(self,pin):
        if self.pin !=pin:
            print('Incorrect pin! Try again.')
            return False
        print(f'You have ${self.amount} in your bank account, dear {self.accountHolder}')
        return self

    def deposit(self, pin, vleraRe):
        if self.pin != pin:
            print('Incorrect pin! Try again.')
            return False
        self.amount=self.amount+int(vleraRe)
        print(f'You have succesfully deposited ${self.amount} in your bank account.')

    def withdraw(self, pin, vleraTerheqjes):
        if self.pin !=pin:
            print('Incorrect pin! Try again.')
            return False
        if self.amount > self.amount - int(vleraTerheqjes):
            self.amount=self.amount-int(vleraTerheqjes)
            print(f'You have succesfully withdrawed ${vleraTerheqjes} in your bank account.')
            print(f'Current balance: ${self.amount}')
            return self
        else:
            print(f'Insufficient funds. Current balance: ${self.amount}')
            return self  
        
    def interestRate(self, pin, interestRate):
        if self.pin !=pin:
            print('Incorrect pin! Try again.')
            return False
        if self.amount > 0:
            self.amount=self.amount+(self.amount*int(interestRate))
        else:
            print(f'Insufficient funds. Current balance: ${self.amount}')
            return self