"""
Ask a number from user. Tell if the number
is prime or not
"""
# num = int(input("Enter number:"))
# count = 0
# for i in range(1, num+1):
#     if num % i == 0:
#         count += 1
# if count == 2:
#     print("Prime number")
# else:
#     print("Not a Prime number")

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
# num = 1
# for i in range(1, 6):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

"""
. . . . *
. . . * *
. . * * *
. * * * *
* * * * *
for(no. of lines)
   for(spaces)
   for(stars)
"""
for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")

    for k in range(1, i+1):
        print("*", end=" ")

    print()

# OR SOLUTION:
i = 1
j = 5
while j > 0:
    print(j*".", i*"*")
    j = j-1
    i = i+1
