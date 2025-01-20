class BankAccount:
    def __init__(self,account_balance = 0):
        self.account_balance = account_balance

    def deposit(self,amount):
        deposit = self.account_balance + amount
        return f"Deposited: ${amount}"

    def withdraw(self,amount):
        if amount > self.account_balance :
            print("Insufficient funds.")
            return False
        else :
           withdraw = self.account_balance - amount
        print(f"Withdrawn: ${withdraw}")
        return True
    
    def display_balance(self):
       print(f"Current Balance: ${self.account_balance}")

