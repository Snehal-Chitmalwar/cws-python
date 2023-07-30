# common in set
a = {54, 23, 68, 39, 90, 41}
b = {23, 51, 67, 38, 633}
# print(a.union(b))  # mixture of a n b
print(a.intersection(b))

# common in list
a = [54, 23, 68, 39, 90, 41]
b = [23, 51, 67, 38, 633]
print(set(a).intersection(set(b)))


# string to set
string = "Goood Morning"
a = set(string)
print(a)
