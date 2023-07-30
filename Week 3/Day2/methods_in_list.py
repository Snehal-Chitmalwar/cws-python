a = [45, 23, 89, 78, 88, 45]
# add element at last
a.append("1000")
print(a)

# add element at any position
a.insert(-22, -100)
print(a)

"""
# make a empty list
using for loop,ask 10 numbers from user
add every number to the list
print list
"""
# a = []
# for i in range(10):
#     num = int(input("Enter number:"))
#     a.append(num)
# print(a)

# count no of elements
print(a.count(890))

# delete element by position
# a.pop(0)
# print(a)
# a.pop()  # deletes last element when pop index is empty
# print(a)
# a.pop(-2)
# print(a)
a.remove(45)
print(a)


"""

"""

a = [34, 45, 56, 23, 57, 7, 87, 34, 34, 65, 67, 97]
num = int(input("Enter number to be removed:"))
while a.count(num) != 0:
    a.remove(num)
print(a)
