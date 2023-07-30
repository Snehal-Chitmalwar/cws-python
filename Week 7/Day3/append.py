file_name = input("Enter file name w/o extension:")
data = input("Enter sentence you want to write:")
f = open(file_name+".txt", "w")
f.write(data)
f.close()


# append
# f = open(file_name+".txt", "a")
# f.write("Good")
# f.close()

"""
Ask two numbers from user 5 14
result.txt

5 odd
6 even
7 odd
8 even
.
.
14 even

"""
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
f = open("result.txt", "a")
for i in range(num1, num2+1):
    if i % 2 == 0:
        f.write(f"{i} even\n")
    else:
        f.write(f"{i} odd\n")
f.close()

"""
find total of all numbers in good
"""
f = open("good.txt", "r")
my_list = []
for i in f.readlines():
    my_list.append(int(i.strip()))
print(sum(my_list))
