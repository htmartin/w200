# For this challenge, create a bank account class that has two attributes:
# owner
# balance

# and two methods:
# deposit
# withdraw

# As an added requirement, withdrawals may not exceed the available balance.

class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance= balance
    
    #method:deposit
    def deposit(self,amount):
        self.balance += amount
    
    # method: withdraw
    def withdraw(self,amount):
        self.balance -=amount
            
            

        
acct1= Account('bob', 300)
print(acct1.balance)
300
acct1.deposit(100)
print(acct1.balance)
200
acct1.withdraw(200)
print(acct1.balance)
200
    
    