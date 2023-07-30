# enter 2 numbers=45 20
# 65
inputstr = input("Enter 2 numbers:")
array = inputstr.split()
print(array)
sum = 0
for i in array:
    sum += int(i)
print(sum)
