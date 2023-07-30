# Q1. Store name as a Key, and 5 marks in a List as a value in dictionary.
# Store details of at least 5 students. Print the total marks with percentage of each and every student.
my_dict = {"John": [89, 56, 78, 56, 45], "Tom": [78, 56, 45, 34, 34], "James": [
    45, 89, 90, 67, 56], "Rose": [45, 89, 67, 78, 67], "Jasmine": [90, 89, 78, 67, 56]}
for k, v in my_dict.items():
    print(f"{k} : Sum={sum(v)}, Percentage={(sum(v)/500)*100}")
print()

# Q2. Store name as a Key, and 5 marks in a List as a value in dictionary.
#  Store details of at least 5 students. Print the name of the student who got highest marks
my_dict = {"John": [89, 56, 78, 56, 45], "Tom": [78, 56, 45, 34, 34], "James": [
    45, 89, 90, 67, 56], "Rose": [45, 89, 67, 78, 67], "Jasmine": [90, 89, 78, 67, 56]}
maximum = max(my_dict.values())
for k, v in my_dict.items():
    if v == maximum:
        print(f"The student who got highest marks is: {k}")
        break

# Q3. Store name as a Key, and 5 marks in a List as a value in dictionary.
# Store details of at least 5 students. Print only the total marks of every student in ascending order.
my_dict = {"John": [89, 56, 78, 56, 45], "Tom": [78, 56, 45, 34, 34], "James": [
    45, 89, 90, 67, 56], "Rose": [45, 89, 67, 78, 67], "Jasmine": [90, 89, 78, 67, 56]}
marks_list = []
for k, v in my_dict.items():
    marks_list.append(sum(v))
marks_list.sort()
print(marks_list)

# Q4. Store name as a Key, and 5 marks in a List as a value in dictionary.
# Store details of at least 5 students. Print the highest marks of every individual student
my_dict = {"John": [89, 56, 78, 56, 45], "Tom": [78, 56, 45, 34, 34], "James": [
    45, 89, 90, 67, 56], "Rose": [45, 89, 67, 78, 67], "Jasmine": [90, 89, 78, 67, 56]}
for k, v in my_dict.items():
    print(f"The highest marks of {k} is {max(v)}")
print()
