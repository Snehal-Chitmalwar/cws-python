# Q.1.Check if the number entered by user is divisible by 3 or not
num = int(input("Enter your number: "))
if num % 3 == 0:
    print(f"{num} is divisible by 3")
else:
    print(f"{num} is not divisible by 3")

# Q.2.Check if the number entered by User is odd or even
num = int(input("Enter your number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Q.3.Take values of length and breadth of a rectangle from user and check if it is square or not
length = int(input("Enter length of a rectangle: "))
breadth = int(input("Enter breadth of a rectangle: "))
if length == breadth:
    print(
        f"The rectangle with length {length} and  breadth {breadth} is a square")
else:
    print(
        f"The rectangle with length {length} and  breadth {breadth} is not  a square")

# Q.4.A school has following rules for grading system:
# a) Below 25-F
# b) 25 to 45-E
# c) 45 to 50-D
# d) 50 to 60-C
# e) 60 to 80-B
# f) above 80-A
# Ask user to enter marks and print the corresponding grade
history = int(input("Enter marks for history: "))
civics = int(input("Enter marks for civics: "))
hindi = int(input("Enter marks for hindi: "))
total = history+civics+hindi
percent = (total/300)*100
if percent < 25:
    grade = "F"
elif percent >= 25 and percent <= 45:
    grade = "E"
elif percent > 45 and percent <= 50:
    grade = "D"
elif percent > 50 and percent <= 60:
    grade = "C"
elif percent > 60 and percent <= 80:
    grade = "B"
elif percent > 80:
    grade = "A"
print(f"Your total marks are {total}")
print(f"Your grade is {grade}")

# Q.5.A student will not be allowed to sit in exam if his/her attendance is less than 75%
# Take following input from user:
# Number of classes held
# Number of classes attended
# And print percentage of class attended
# Tell if student is allowed to sit in exam or not?
Classes_held = int(input("Enter total number of classes held: "))
Classes_attended = int(input("Enter total number of classes attended: "))
percent = (Classes_attended/Classes_held)*100
if percent >= 75:
    print(f"The student is allowed to sit in exam.")
else:
    print(f"The student is not allowed to sit in exam.")
