a = [56, 43, 12, 65, 56, 56, 47, 0, 877, 65, 48, 99]
num = int(input("Enter number:"))
count = 0
for i in range(0, len(a)):
    if a[i] == num:
        count += 1
print(count)
