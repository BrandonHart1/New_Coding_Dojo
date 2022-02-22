
# Create a file with the User class, including the __init__ and make_deposit methods

class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount


# Add a make_withdrawal method to the User class

    def make_withdrawel(self, amount):
        self.account_balance -= amount


# Add a display_user_balance method to the User class

    def display_user_balance(self):
        print(self.account_balance)

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount 


billy = User("Billy")
bob = User("Bob")
thorton = User("Thorton")

billy.make_deposit(100)
billy.make_deposit(200)
billy.make_deposit(300)
billy.make_deposit(400)
billy.make_withdrawel(200)
billy.display_user_balance()

bob.make_deposit(200)
bob.make_deposit(300)
bob.make_deposit(400)
bob.make_withdrawel(100)
bob.display_user_balance()


thorton.make_deposit(300)
thorton.make_deposit(400)
thorton.make_deposit(500)
thorton.make_withdrawel(50)
thorton.display_user_balance()





# Create 3 instances of the User class

# Have the first user make 3 deposits and 1 withdrawal and then display their balance

# Have the second user make 2 deposits and 2 withdrawals and then display their balance

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
