a = [56, 43, 12, 65, 56, 56, 47, 877, 65, 48, 99]
b = []
for i in range(0, len(a)):
    if b.count(a[i]) == 0:
        b.append(a[i])
print(b)
