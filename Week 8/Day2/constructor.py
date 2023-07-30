"""
Constructor
Method which runs when object is created
"""


class Bank:

    # def __init__(self):  # Constructor
    #     self.name = input("Enter your account name:")
    #     self.accountNo = input("Enter your account number:")
    #     self.balance = 0

    def __init__(self, n, a):  # Constructor
        self.name = n
        self.accountNo = a
        self.balance = 0

    # def setInfo(self):
    #     self.name = input("Enter your account name:")
    #     self.accountNo = input("Enter your account number:")
    #     self.balance = 0

    def display(self):
        print(
            f"Your name is {self.name} and account number is {self.accountNo}")


x = Bank("snehal", 897897)
# x.setInfo()
# print(x.name)
x.display()
