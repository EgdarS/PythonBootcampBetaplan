class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance=self.balance + int(amount)
        return self
    def withdraw(self, amount):
        if self.balance<int(amount):
            print('Insufficient funds.')
            return self
        self.balance=self.balance-int(amount)
        return self
    def display_account_info(self):
        print(f'Your account balance is ${self.balance}')
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance=self.balance+(self.balance*int(self.int_rate))
            return self
        else:
            return self