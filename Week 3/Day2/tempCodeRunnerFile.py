a = [34, 45, 56, 23, 57, 7, 87, 34, 34, 65, 67, 97]
num = int(input("Enter number to be removed:"))
while a.count(num) != 0:
    a.remove(num)
print(a)