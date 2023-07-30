# Q1. Write a Python program that takes a user's input for a string
# and counts the occurrence of each character in the string. The
# program should then print a dictionary with characters as keys
# and their respective counts as values.
string = input("Enter a string:")
Occurence_dict = {}
for i in string:
    Occurence_dict[i] = string.count(i)
print(Occurence_dict)

# Q2. Write a Python program that takes a user's input for a
# dictionary containing keys as student names and values as their
# grades. The program should print the name of the student with the
# highest grade.
my_dict = {}
range_student = int(
    input("Enter number of students you want to add in a dictionary:"))
for i in range(range_student):
    name = input("Enter student's name:")
    grade = int(input("Enter student's grade:"))
    my_dict[name] = grade
highest_grade = max(my_dict.values())
for k, v in my_dict.items():
    if v == highest_grade:
        print(k)
        break

# Q3. Write a Python program that takes a user's input
# for a dictionary where the keys are student names and
# the values are lists of their test scores.
#  The program should print a new dictionary with the
# student names as keys and their average test scores
# as values.
range_student = int(
    input("Enter number of students you want to add in a dictionary:"))
student_data = {}
average_dict = {}
for i in range(range_student):
    name = input("Enter the name of student:")
    test_scores = []
    for j in range(4):
        mark = int(input("Enter the mark for subject :"))
        test_scores.append(mark)
    student_data[name] = test_scores
for k, v in student_data.items():
    average_dict[k] = sum(v)/len(v)

print("Student Average:", average_dict)

# Q4. Write a Python program that takes a user's input
#  for a dictionary where the keys are categories, and
#  the values are lists of items belonging to that
#  category. The program should also take another input
#  for an item. The program should return the category
# to which the item belongs. If the item does not
# belong to any category, return "The item does not
# belong to any category."
range_category = int(
    input("Enter number of categoriies you want to add in a dictionary:"))
my_data = {}
for i in range(range_category):
    category = input("Enter the category:")
    values = []
    for j in range(4):
        value = input("Enter the value for category :")
        values.append(value)
    my_data[category] = values
item = input("Enter the item name you wish to search:")
for k, v in my_data.items():
    if v.count(item) > 0:
        print(k)
        break
