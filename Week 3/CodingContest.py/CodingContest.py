# Q1. Write a Python program that takes two lists as
# input and prints a new list that contains only the
# elements that are common to both input lists.
# (Take 7 inputs in both lists using for loop and append)
list1 = []
list2 = []
Common = []
for i in range(7):
    l1 = int(input("Enter element to be added in list 1:"))
    list1.append(l1)
    l2 = int(input("Enter element to be added in list 2:"))
    list2.append(l2)
print(list1)
print(list2)
for i in list1:
    if list2.count(i) == 1:
        Common.append(i)
print(f"Common elements: {Common}")

# Q2. Write a Python program that takes a list of
# numbers as input and prints the second largest
# number in the list.
# (Take 10 inputs in both lists using for loop and append)
my_list = []
for i in range(10):
    num = int(input("Enter number to be entered in my_list:"))
    my_list.append(num)
print(my_list)
my_list.sort()
my_list.reverse()
print(f"The second largest number in the list is {my_list[1]}")

# Q3. Write a program which take 10 inputs from user and store it in a list.
# Remember you can input any data types.
# Print only elements which have data type of String.
my_list = [45, 3, True, "CWS", 56, 89, "Hello", False, 78, 98]
for i in my_list:
    datatype = type(i)
    # print(datatype)
    if str(datatype) == "<class 'str'>":
        print(i)

# Q4. Write a Python program that takes a list of
# numbers as input and prints a new list that contains
# only the prime numbers in the input list.
# (Take 10 inputs in a list using for loop and append)
my_list = []
count = 0
new_list = []
for i in range(10):
    num = int(input("Enter number to be entered in my_list:"))
    my_list.append(num)
print(my_list)
for i in my_list:
    j = 2
    while j <= i:
        if i % j == 0:
            count += 1
        j += 1
    if count == 1:
        new_list.append(i)
        # print(i)
    count = 0
print(new_list)

# Q5. Write a Python program that has a list of
# number and print a new list that contains the
# cumulative sum of the input list. For example,
# if the input list is [1, 2, 3, 4], the output should
# be [1, 3, 6, 10].
my_list = [2, 3, 45, 7]
new_list = []
sum = 0
for i in range(0, len(my_list)):
    sum += my_list[i]
    new_list.append(sum)
print(f"Cumulative sum  of the list: {new_list}")

# Q6. Write a Python program that takes a list of
# numbers as input and returns a new list that contains
# all the possible pairs of elements from the input list
# whose sum is even, using list comprehension.
# For example, if the input list is [1, 2, 3, 4],
# the output should be [(1, 3), (1, 4), (2, 4), (3, 1), (3, 2), (4, 2)].
my_list = []
new_list = []
sum_list = []
length = int(input("Enter the length of list:"))
for i in range(length):
    num = int(input("Enter number to be entered in my_list:"))
    my_list.append(num)
print(my_list)
for i in range(0, len(my_list)):
    num = my_list[i]
    for j in my_list:
        sum = j+num
        if j == num:
            continue
        if sum % 2 == 0:
            # element="("&str(num)&","&str(j)&")"
            sum_list.append(num)
            sum_list.append(j)
            if new_list.count(sum_list) == 0:
                new_list += sum_list
                sum_list.clear()
print(f"Pairs of elements whose sum is even: {new_list}")
