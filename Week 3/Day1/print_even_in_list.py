# print even numbers
a = [23, 45, 34, 67, 78, 89]
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        print(a[i], end=" ")

# divisible by 2 n 5
a = [23, 45, 34, 67, 78, 89]
for i in range(0, len(a)):
    if a[i] % 2 == 0 or a[i] % 5 == 0:
        print(a[i])
