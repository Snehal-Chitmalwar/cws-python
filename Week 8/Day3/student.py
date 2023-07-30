"""
Student
name,age,roll,science,english,maths(init)

display()
displayMarks() -> marks only, total marks
updateName() -> new name
updateMarks() -> update sci,eng n mths

menu:
1)add student
2)view all students
3)search a student
4)display marks
5)update name
6)update Marks
7)exit
"""
from random import randint


class Student:

    def __init__(self):
        self.name = input("Enter student name:")
        self.age = int(input("Enter student age:"))
        self.rollNo = int(input("Enter student roll number:"))
        self.science = randint(1, 100)
        self.english = randint(1, 100)
        self.maths = randint(1, 100)

    def display(self):
        print(f"\nSTUDENT INFORMATION:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll No: {self.rollNo}")
        print(f"Marks for Science subject: {self.science}")
        print(f"Marks for English subject: {self.english}")
        print(f"Marks for Maths subject: {self.maths}")

    def displayMarks(self):
        print(
            f"Score of {self.name} are:\nScience: {self.science}\nEnglish: {self.english}\nMaths: {self.maths}")
        print(
            f"The total marks scored are: {self.science+self.english+self.maths}/300")

    def updateName(self):
        self.name = input("Enter new name:")
        self.display()

    def updateMarks(self):
        self.science = int(input("Enter new Science marks:"))
        self.english = int(input("Enter new English marks:"))
        self.maths = int(input("Enter new Maths marks:"))
        self.display()


records = []

while True:
    print("Welcome to Record Book of this year!")
    print("1) Add student")
    print("2) View all students")
    print("3) Search a student")
    print("4) Display marks")
    print("5) Update Name")
    print("6) Update Marks")
    print("7) Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        newStudent = Student()
        records.append(newStudent)
        print(f"Student list in records: {records}")
    elif choice == 2:
        if len(records) == 0:
            print("No student information is added yet to the record")
        else:
            for i in records:
                i.display()
    elif choice == 3:
        searchStudent = input("Enter student name you want to search:")
        for i in records:
            if i.name == searchStudent:
                i.display()
    elif choice == 4:
        searchStudent = input("Enter student name you wish to see marks for:")
        for i in records:
            if i.name == searchStudent:
                i.displayMarks()
    elif choice == 5:
        searchStudent = input("Enter student name you wish to update name of:")
        for i in records:
            if i.name == searchStudent:
                i.updateName()
    elif choice == 6:
        searchStudent = input(
            "Enter student name you wish to update marks of:")
        for i in records:
            if i.name == searchStudent:
                i.updateMarks()
    elif choice == 7:
        break
    else:
        print("Invalid choice")
