# Encapsulation is the bundling of data (attributes) and methods that operate on that data into a single unit (class).
# It also involves restricting direct access to some components (using private/protected members).
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# TASK: Make sure balance cannot be accessed or modified directly from outside.
# Fix the class by properly encapsulating the balance attribute.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # <-- Should be private

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

# Test
acc = Account("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc.balance)  # <-- Should not access like this!
