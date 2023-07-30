a = [54, 23, 56, 67, 78]
# print(id(a))  # -- prints location of memory

# removees all elements from list
# a.clear()
# print(a)

# b = a
# a.pop(2)  # removes element from both variables
# print(a, b)

b = a.copy()
print(id(a))
print(id(b))