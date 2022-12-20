class Account:
    def __init__(self, balance):
        # sets the balance from input
        self.balance = balance

    def deposit(self, amount):
        # adds an amount to balance
        self.balance += amount

    def withdraw(self, amount):
        # takes an amount from balance
        self.balance -= amount

    def get_balance(self):
        # returns how much is balance
        return self.balance

