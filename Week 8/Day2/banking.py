from random import choice
from random import randint


class Bank:

    def __init__(self):
        self.accNo = randint(100000, 2000000)
        self.name = input("Enter account name:")
        self.balance = 1000

    def deposit(self):
        price = int(input("Enter amount to deposit:"))
        self.balance = self.balance+price

    def withdraw(self):
        price = int(input("Enter amount to withdraw:"))
        if price <= self.balance:
            self.balance = self.balance-price
        else:
            print("Insufficient Balance")

    def display(self):
        print("\nACCOUNT INFO\n")
        print(f"name = {self.name}")
        print(f"Account Number = {self.accNo}")
        print(f"Balance = {self.balance}")
        print()

    def displayBalance(self):
        print(f"Your balance: {self.balance}")


x = Bank()
x.display()
x.withdraw()
x.displayBalance()
x.deposit()
x.displayBalance()


# code:

string = "abcdefghi1234567890"

randomAcc = [choice(string).upper() for _ in range(5)]
print(randomAcc)
result = "-".join(randomAcc)
print(result)
