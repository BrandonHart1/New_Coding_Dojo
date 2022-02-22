class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

# deposit amount and new balance.
    def deposit(self, amount):
        self.balance += amount
        print(f"Total after deposit = {self.balance}")
        return self
# display the withdrawel amount and new balance
    def withdraw(self, amount):
        if amount <= 0 or self.balance - amount <= 0:
            print("Insufficient funds")
        else:
            self.balance -= amount
        print(f"Total after withdrawel = {self.balance}")
        return self

# display the account balance
    def display_account_info(self):
        print("Balance " + self.balance)

# interest rate added to balance
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            print(f"After interest = {self.balance}")


# print("anything")
billy = BankAccount(.01, 50)
bob = BankAccount(.01, 75)

billy.deposit(100).deposit(200).deposit(300).withdraw(200).yield_interest()

bob.deposit(200).deposit(300).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest()