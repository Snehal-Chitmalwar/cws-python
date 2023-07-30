# Q1. Ask 10 numbers from the user and put them into the list. After that remove all the duplicates from that list.
a = []
b = []
for i in range(10):
    num = int(input("Enter the number:"))
    a.append(num)
print(a)
for i in range(0, len(a)):
    if b.count(a[i]) == 0:
        b.append(a[i])
print(b)

# Q2. Write a Python program to check a list is empty or not.
a = [1, 23, 23, 34]
if len(a) == 0:
    print(f"The list is empty")
else:
    print(f"The list is not empty")

# Q3. Make 2 different list. Check if they have at least one common number. If they have at least 1 common number, print “YES” else print “NO”
a = [44, 56, 43, 11, 12, 34]
b = [78, 66, 55, 44]
exists = False
for i in a:
    if b.count(i) > 0:
        exists = True
        break

if exists == True:
    print("Yes")
else:
    print("No")

# Q4. Ask 10 numbers from the user and put them into the list. Now remove all the even numbers from that list.
a = []
b = []
for i in range(10):
    num = int(input("Enter the number:"))
    a.append(num)
print(a)
for i in range(0, len(a)):
    if a[i] % 2 != 0:
        b.append(a[i])
print(b)

# Q5. Write a Python program to find the second smallest number in a list.
a = [44, 56, 43, 11, 12, 34]
a.sort()
print(f"The second smallest number in a list is {a[1]}")

# Q6. Write a Python program to find the second largest number in a list.
a = [44, 56, 43, 11, 12, 34]
a.sort()
print(f"The second smallest number in a list is {a[len(a)-2]}")

# Q7. Write a python program which prints all the values whose count is greater than 3. (Make sure to make a list with at least 15 numbers)
a = [12, 12, 12, 34, 4, 5, 6, 6, 7, 6, 6, 7, 45, 2, 90]
b = []
for i in range(0, len(a)):
    if a.count(a[i]) > 3 and b.count(a[i]) == 0:
        b.append(a[i])
print(b)

# Q8. Write a Python program to add an item in a tuple.
a = (54, 85, 74, 10, 6, 56, 56)
b = list(a)
b.append(23)
a = tuple(b)
print(a)

# Q9. Write a Python program to find the repeated items of a tuple.
a = (54, 85, 74, 10, 6, 56, 56)
b = []
for i in range(0, len(a)):
    if a.count(a[i]) > 1 and b.count(a[i]) == 0:
        b.append(a[i])
print(b)

# Q10. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
a = []
for i in range(10):
    num = int(input("Enter the number:"))
    a.append(num)
print(a)
a.reverse()
b = a.copy()
print(b)

# Q11. Write a program to find the average of all the numbers present in the list.
a = [44, 56, 43, 11, 12, 34]
sum = 0
for i in range(0, len(a)):
    sum += a[i]
avg = sum/len(a)
print(f"The average of all numbers in list is: {avg}")

# Q12. Make 2 different list. First merge both list into third variable. And sort the merge list in descending order.
a = [44, 56, 43, 11, 12, 34]
b = [45, 78, 44, 56, 43, 11, 12, 34]
c = a+b
c.sort()
c.reverse()
print(c)

# Q13. Find the common elements between two lists.
a = [44, 56, 43, 11, 12, 34]
b = [78, 66, 55, 44]
exists = False
for i in a:
    if b.count(i) > 0:
        print(i)

# Q14. Make a list. Write a simple program for addition of the 2nd element from start and 2nd element from the end.
a = [44, 56, 43, 11, 12, 34]
sum = a[1]+a[-2]
print(sum)

# Q15. What’s the difference between append, extend and insert?
"""
append-> it'll add an element in the last of any list
insert-> it'll add any element at the given index in the list
extend-> it'll add any other list at the end of current list
"""
