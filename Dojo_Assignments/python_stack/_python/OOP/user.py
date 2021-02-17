class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount


troy = User("Troy", "troy@python.com")
mike = User("Mike", "mike@python.com")
kevin = User("Kevin", "kevin@python.com")

troy.make_deposit(100).make_deposit(200).make_deposit(
    300).make_withdrawal(200).display_user_balance()

mike.make_deposit(200).make_deposit(400).make_withdrawal(
    300).make_withdrawal(100).display_user_balance()

kevin.make_deposit(5000).make_withdrawal(1000).make_withdrawal(
    500).make_withdrawal(500).display_user_balance()

kevin.transfer_money(mike, 1000)
kevin.display_user_balance()
mike.display_user_balance()
