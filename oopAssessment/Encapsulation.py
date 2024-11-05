class BankAccount:
    def __init__(self,balance=0):
        self._balance = balance

    def deposit(self,amount):
        self._balance += amount

    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print ("Insufficient funds")

    def get_balance(self):
        return self._balance

my_account = BankAccount(100000)
my_account.deposit(50000)
my_account.withdraw(10000)
print(my_account.get_balance())