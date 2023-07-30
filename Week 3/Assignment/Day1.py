# Q1. Reverse a list in Python without using reverse().
a = [23, 3, 4, 45, 56, 86]
b = []
for i in range(len(a)-1, -1, -1):
    b.append(a[i])
print(b)

# Q2. Make 3 lists. Merge all the 3 lists in one list.
a = [23, 3, 4, 45, 56, 86]
b = [34, 56, 89, 56]
c = [78, 90, 67, 45, 67]
d = a+b+c
print(d)

# Q3. Make a list. Tell if the length of that list is Even or Odd.
a = [23, 3, 4, 45, 56, 86]
if len(a) % 2 == 0:
    print("The length of the list is even")
else:
    print("The length of the list is odd")

# Q4. Make a list. Find the sum of all the elements in list which are divisible by 3.
a = [23, 3, 4, 45, 56, 86]
sum = 0
for i in range(0, len(a)):
    if a[i] % 3 == 0:
        sum += a[i]
print(f"The sum of elements in list which are divisible by 3 is {sum}")

# Q5. Make a list. Find how many positive and negative numbers are there.
a = [23, 67, -78, 67, -56, -87]
positive = 0
negative = 0
for i in range(0, len(a)):
    if a[i] < 0:
        positive += 1
    else:
        negative += 1
print(
    f"There are {positive} positive numbers and {negative} negative numbers.")

# Q6. Make a list. Print the maximum/greatest number from that list.
a = [23, 3, 4, 45, 56, 86]
maximum = max(a)
print(f"The maximum/greatest number from that list is {maximum}")
# or
a = [23, 3, 4, 45, 56, 86]
maximum = a[0]
for i in range(0, len(a)):
    if a[i] > maximum:
        maximum = a[i]
print(f"The maximum/greatest number from that list is {maximum}")

# Q7. Make a list. Print the minimum/smallest number from that list.
a = [23, 3, 4, 45, 56, 86]
minimum = min(a)
print(f"The minimum/smallest number from that list is {minimum}")
# or
a = [23, 3, 4, 45, 56, 86]
minimum = a[0]
for i in range(1, len(a)):
    if a[i] < minimum:
        minimum = a[i]
print(f"The minimum/smallest number from that list is {minimum}")
