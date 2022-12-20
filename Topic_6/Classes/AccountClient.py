# imports Account class from another file
from Account import Account

# Define how much balance is in an account names some account
some_account = Account(1000.00)
# calls deposit method from class Account to add to balance
some_account.deposit(550.23)
# -//-
some_account.deposit(100)
# calls withdraw method from class Account to take from balance
some_account.withdraw(50)
# calls getbalance method from class Account to print remaining balance
print(some_account.get_balance())
# makes a new Account object that has 0 balance
another = Account(0)
# calls a question to name the class of another object
print("object another is class", another.__class__.__name__)
