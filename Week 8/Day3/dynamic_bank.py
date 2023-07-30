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


accounts = []

while True:
    print("\n1) Create Account")
    print("2) Display all Accounts")
    print("3) Search an Accounts")
    print("4) Deposit")
    print("5) Withdraw")
    print("6) Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        newObj = Bank()
        accounts.append(newObj)
        print(f"Accounts list={accounts}")
    elif choice == 2:
        if len(accounts) == 0:
            print("No accounts added yet")
        else:
            for i in accounts:
                i.display()
    elif choice == 3:
        searchAccNo = int(input("Enter account number you want to search:"))
        for i in accounts:
            if i.accNo == searchAccNo:
                i.display()
    elif choice == 4:
        searchAccNo = int(input("Enter account number you want to deposit:"))
        for i in accounts:
            if i.accNo == searchAccNo:
                i.deposit()
                i.displayBalance()
    elif choice == 5:
        searchAccNo = int(input("Enter account number you want to withdraw:"))
        for i in accounts:
            if i.accNo == searchAccNo:
                i.withdraw()
                i.displayBalance()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
