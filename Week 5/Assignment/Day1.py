# Q1. Find the sum of all items (values) in a dictionary without using sum.
my_dict = {"John": 89, "Tom": 78, "James": 45}
sum = 0
for i in my_dict.values():
    sum += i
print(f"The sum of the dictionary values is: {sum}")

# Q2. Store “name” of a student as Key, “list of 5 marks” of that student as a Value.
# Store atleast 5 student names. Print the sum and percentage of all the students
my_dict = {"John": [89, 56, 78, 56, 45], "Tom": [78, 56, 45, 34, 34], "James": [
    45, 89, 90, 67, 56], "Rose": [45, 89, 67, 78, 67], "Jasmine": [90, 89, 78, 67, 56]}
for k, v in my_dict.items():
    print(f"{k} : Sum={sum(v)}, Percentage={(sum(v)/500)*100}")
print()

# Q3. Store marks of 5 different subjects in a dictionary. Print the second highest marks
my_dict = {"English": 45, "Hindi": 78, "Science": 67, "Maths": 90, "CS": 89}
maximum = max(my_dict.values())
for k, v in my_dict.items():
    if v == maximum:
        my_dict.pop(k)
        break
print(f"The second highest marks are: {max(my_dict.values())}")

# Q4. Store marks of 5 different subjects in a dictionary. Append all those
# marks in a different list and print that list in ascending order.
my_dict = {"English": 45, "Hindi": 78, "Science": 67, "Maths": 90, "CS": 89}
marks_list = []
for v in my_dict.values():
    marks_list.append(int(v))
print(marks_list.sort())
print(marks_list)

# Q5. Store marks of 5 different subjects in a dictionary. Ask subject name as an input from the User.
# Print the marks of that subject entered by User. If subject does not exist, print “Invalid”.
my_dict = {"English": 45, "Hindi": 78, "Science": 67, "Maths": 90, "CS": 89}
subject = input("Enter a subject:").lower()
presentflag = False
for k, v in my_dict.items():
    if k.lower() == subject:
        print(f"The marks for {k} subject is {v}")
        presentflag = True
        break
if presentflag != True:
    print("Invalid")
