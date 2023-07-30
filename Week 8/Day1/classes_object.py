"""
Class (Student)
name,roll, gender

Book
author,subject,genre,price,language
"""


class Student:
    # Data members-variable inside class
    # name = ''
    # age = 0
    # gender = ''

    # method
    def setInfo(self):
        self.name = input("Enter name:")
        self.age = int(input("Enter age:"))
        self.gender = input("Enter gender:")

    def setInfo2(self, n, a, g):
        self.name = n
        self.age = a
        self.gender = g

    def display(self):
        print(f"Your name is {self.name}")
        print(f"Your age is {self.age}")
        print(f"Your gender is {self.gender}")

    def updateAge(self):
        self.age = input("Enter age:")

    def eligibility(self):
        if self.age > 18:
            print(f"{self.name} - You're adult")
        else:
            print(f"{self.name} - You're child")


# obj1 = Student()  # object created
# obj1.setInfo()
# obj1.display()
# obj1.eligibility()
obj2 = Student()
obj2.setInfo2("abc", 90, "male")
obj2.display()
