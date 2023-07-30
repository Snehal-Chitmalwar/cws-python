a = "Good morning"
list(a)
# b = list(a)
b = []

for i in range(0, len(a)):
    if a.count(a[i]) == 1:
        b.append(a[i])
print(b)
