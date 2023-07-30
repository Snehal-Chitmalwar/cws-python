a = [45, 31, 56, 78, 66, 45, 77, 12, 65]
# b = [i+5 for i in a]
# print(b)
# b = [i for i in a if i % 2 == 0]
# print(b)
b = [[i-5, i, i+5] for i in a]
print(b)


# [1,4,9,16,25...100]
a = [i**2 for i in range(1, 11)]
print(a)
