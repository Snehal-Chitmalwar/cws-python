# Q1. Write a Python class named Book with a constructor that takes  a title,
# an author, and a price as arguments and initializes three  instance variables,
# title, author, and price. Write a method named  discount that applies a discount
# to the price and returns the  discounted price.
from random import randint


class Book:
    def __init__(self, book_title, book_author, book_price):  # Constructor
        self.title = book_title
        self.author = book_author
        self.price = book_price

    def discount(self):
        discount = randint(10, 80)
        self.discount_price = self.price-(self.price*(discount/100))
        print(
            f"Woohooo!! You got {discount/100}% discount.")
        return self.discount_price


objBook = Book("Civics", "XYZ", 500)
print(f"You just need to pay Rs/-{objBook.discount()}")

# Q2. Write a Python class named Employee with a constructor that  takes a name,
# an age, a salary, and a department as arguments  and initializes four instance
# variables, name, age, salary, and  department. Write a method named promote that
# increases the  salary of the employee by a certain percentage.


class Employee:
    def __init__(self, emp_name, emp_age, emp_salary, emp_depart):  # Constructor
        self.name = emp_name
        self.age = emp_age
        self.salary = emp_salary
        self.department = emp_depart

    def promote(self):
        inc_percent = randint(5, 50)
        self.inc_sal = self.salary+(self.salary*(inc_percent/100))
        return self.inc_sal


objEmp = Employee("John", 23, 50000, "IT")
print(objEmp.promote())

# Q3. Write a Python class named Rectangle with a constructor that  takes no
# arguments and prompts the user for the length and width  of the rectangle.
#  The constructor should initialize two instance  variables with the same names.
# Write a method named area that  calculates and returns the area of the rectangle.


class Rectangle:
    def __init__(self):
        self.length = int(input("Enter length of rectangle:"))
        self.width = int(input("Enter width of rectangle:"))

    def area(self):
        self.area = self.length*self.width
        return self.area


obj_rect1 = Rectangle()
print(obj_rect1.area())

# Q4. Write a Python class named BankAccount with a constructor  that takes no
#  arguments and prompts the user for an initial  balance and an account number.
# The constructor should initialize  two instance variables, balance and accountNumber.
#  Write  methods named deposit and withdraw that allow the user to  deposit or withdraw money from the account.


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
            print(self.balance-self.withdraw)
        else:
            print("Insufficient Balance")


objBankAcc = BankAccount()
print(objBankAcc.deposit())
print(objBankAcc.withdraw())
