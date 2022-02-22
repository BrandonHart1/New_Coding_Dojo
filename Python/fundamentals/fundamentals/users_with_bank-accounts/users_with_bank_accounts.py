class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

# deposit amount and add to balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Total after deposit = {self.balance}")
        return self

# depoist amount and subtract from balance
    def withdraw(self, amount):
        if amount <= 0 or self.balance - amount <= 0:
            print("Insufficient funds")
        else:
            self.balance -= amount
        print(f"Total after withdrawel = {self.balance}")
        return self

# display the bank account
    def display_account_info(self):
        print(f"Balance {self.balance}")
        return self

# display the interest (if any earned) and the new balance
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            print(f"After interest = {self.balance}")
        return self
# ______________________________________________________________________
class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate = 0.01, balance = 0)

# make deposit from the BankAccount class
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

# make withdrawel from the BankAccount class
    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self

# display the account info
    def display_account_info(self):
        self.account.display_account_info()
        return self

# interest 
    def yield_interest(self):
        self.yield_interest()
        return self


billy = User("Billy")
bob = User("Bob")
thorton = User("Thorton")

billy.make_deposit(100).make_deposit(200).make_deposit(300).make_deposit(400).withdraw(200).display_account_info()

bob.make_deposit(200).make_deposit(300).make_deposit(400).withdraw(100).display_account_info()

thorton.make_deposit(300).make_deposit(400).make_deposit(500).withdraw(50).display_account_info()