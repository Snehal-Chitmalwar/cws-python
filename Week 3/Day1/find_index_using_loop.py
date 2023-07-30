# print position of entered number
a = [56, 43, 12, 67, 43, 23, 55, 66, 43, 11, 23, 84, 71, 42, 45]
num = int(input("Enter number:"))
for i in range(0, len(a)):
    if a[i] == num:
        print(i)
