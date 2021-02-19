class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Account(int_rate=0.02, balance=0)

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        print(f"User:{self.name} Balance:${self.account.balance}")
        return self

    def yield_interest(self):
        if self.account.balance > 0:
            self.account.balance = (
                self.account.balance + self.account.balance * self.account.interest
            )
        return self


class Account:
    def __init__(self, int_rate=0.02, balance=0):
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
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
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.interest
        return self


troy = User("Troy Dojo", "troy@python.com")
mike = User("Mike Dojo", "mike@python.com")


troy.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawl(
    100
).yield_interest().display_user_balance()

mike.make_deposit(2000).make_deposit(2000).make_withdrawl(200).make_withdrawl(
    200
).yield_interest().display_user_balance()
