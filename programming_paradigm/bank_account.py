class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        amount = int(input("Enter the amount to deposit: "))
        self.account_balance += amount
        print(f"Deposited: ${amount}")
    
    def withdraw(self, amount):
        amount = int(input("Enter amount to withdraw: "))
        if self.account_balance > amount:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    
    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")


