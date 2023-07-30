"""
LOOPS / LOOPING
1) While Loop
2) For Loop

while condition:
    ...
    ...
    ...
    ...
...
"""

# i = 1
# while i <= 10:
#     print("hello world")
#     i = i+1

# i = 1
# while i >= 15:
#     print(i)
#     i = i+1

# i = 1
# while i < 52:
#     print(i, end=" ")
#     i = i+5

# num = int(input("Enter number:"))
# if num > 1:
#     i = 1
#     while i <= num:
#         print(i)
#         i = i+1

# start = int(input("Enter start number:"))
# end = int(input("Enter end number:"))
# if start <= end:
#     while start <= end:
#         print(start)
#         start = start+1

# i = 10
# while i > 0:
#     print(i)
#     i = i-1

# start = int(input("Enter start number:"))
# end = int(input("Enter end number:"))
# if start > end:
#     while start >= end:
#         print(start, end=" ")
#         start = start - 1
# elif start < end:
#     while start <= end:
#         print(start, end=" ")
#         start = start + 1
# else:
#     print("Both are equal")

# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))
# num = 1
# sum = 0
# while num <= 10:
#     sum = sum+num
#     num = num+1
# print(sum)

# num = int(input("Enter number:"))
# sum = 0
# i = 1
# while i <= num:
#     sum = sum+i
#     i = i+1
# print(sum)

# num = int(input("Enter number:"))
# fact = 1
# i = 1
# while i <= num:
#     fact = fact*num
#     num = num-1
# print(fact)

num = int(input("Enter number:"))
i = 0
while num > 0:
    a = num//10
    num = a
    if num >= 0:
        i = i+1
print(i)

print(len(str(int(input("Enter number = ")))))

num = 124  # 546
count = 0
while num != 0:
    count = count+1
    num = num//10
