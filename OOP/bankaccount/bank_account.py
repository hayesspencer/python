class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            return self
        else:
            self.balance -= 0
            print("Insufficient funds:Charge of $35")
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance = self.balance + self.balance * self.interest
        return self


troyAcct = BankAccount()
mikeAcct = BankAccount()

troyAcct.deposit(200).deposit(200).deposit(200).withdraw(
    400).yield_interest().display_account_info()

mikeAcct.deposit(1200).deposit(2200).withdraw(200).withdraw(200).withdraw(
    200).withdraw(200).yield_interest().display_account_info()
