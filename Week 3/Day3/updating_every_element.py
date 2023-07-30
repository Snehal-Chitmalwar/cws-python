a = [56, 43, 12, 65, 56, 56, 47, 0, 877, 65, 48, 99]
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        a[i] += 5
    else:
        a[i] -= 5
print(a)
