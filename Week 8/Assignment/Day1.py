# Q1. Write a Python class named Rectangle with two variables  length and width.
# Write a method named area that calculates  and returns the area of the rectangle.
class Rectangle:

    def set_rect_sides(self):
        self.length = int(input("Enter length of a rectangle:"))
        self.width = int(input("Enter width of a rectangle:"))

    def area(self):
        area = self.length*self.width
        return area


obj_rect1 = Rectangle()
obj_rect1.set_rect_sides()
print(obj_rect1.area())

# Q2. Write a Python class named Car with two instance variables  make and model.
# Write a method named getMakeModel that  returns the make and model of the car as a string.


class Car:

    def set_Car_details(self, car_make, car_model):
        self.make = car_make
        self.model = car_model

    def getMakeModel(self):
        return self.make + "," + self.model


obj_car1 = Car()
obj_car1.set_Car_details("yes", "Honda")
print(obj_car1.getMakeModel())

# Q3. Write a Python class named BankAccount with two instance  variables balance and
# accountNumber. Write methods named  deposit and withdraw that allow the user to deposit
#  or withdraw money from the account.


class BankAccount:

    def set_Acc_details(self, balance, accountNumber):
        self.bal = balance
        self.accNo = accountNumber

    def withdraw(self):
        amt = int(
            input("Enter the ammount you want to withdraw from your bank account:"))
        if amt <= self.bal:
            self.bal -= amt
            self.displayBalance()
        else:
            print("Sorry! You don't have enough balance in your account")

    def deposit(self):
        amt = int(
            input("Enter the ammount you want to deposit in your bank account:"))
        self.bal += amt
        self.displayBalance()

    def displayBalance(self):
        print(f"Your balance now is {self.bal}")


obj_bankAcc1 = BankAccount()
obj_bankAcc1.set_Acc_details(68578678, 586597696976)
obj_bankAcc1.deposit()
obj_bankAcc1.withdraw()
