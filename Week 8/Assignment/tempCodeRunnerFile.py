class BankAccount:
    def __init__(self):
        self.accountNumber = int(input("Enter account number:"))
        self.balance = int(input("Enter balance of your account:"))

    def deposit(self):
        self.deposit = int(input("Enter amount to deposit:"))
        return self.balance+self.deposit

    def withdraw(self):
        self.withdraw = int(input("Enter amount to withdraw:"))
        if self.withdraw <= self.balance:
            return self.balance-self.withdraw
        else:
            print("Insufficient Balance")


objBankAcc = BankAccount()
print(objBankAcc.deposit())
print(objBankAcc.withdraw())
