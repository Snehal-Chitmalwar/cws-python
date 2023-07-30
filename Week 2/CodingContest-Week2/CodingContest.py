# Q.1.
# Ans. a)
# skip the step by 10 to get expected series
for i in range(10, 201, 10):
    print(i, end=" ")

# b)
i = 1
while i <= 100000000:
    print(i, end=" ")
    i = i*10  # muliply each time by 10 to get the expected series

# c)
num = 1
for i in range(11):
    for j in range(i):  # to print the  value of 1 for i number of times in j loop
        print(num, end="")
    print(end=" ")

# d)
i = 1
j = 1
# j is initialized to run loop until expected count of numbers
while j <= 12:
    print(i, end=" ")
    if j % 2 != 0:  # to check if position of number is odd, then add 2 to the number
        i += 2
    else:  # to check if position of number is even, then add 3 to the number
        i += 3
    j += 1

# # Q.2)
# # Ans.
n = int(input("Enter a number:"))
i = 1
sum = 1
while i <= n:
    exp = 2 ** i  # find exponential value
    factor = 1/exp  # find invert ratio of exponential value
    sum = sum+factor  # adding calculated factor value to sum having value as 1 already
    i += 1
print(sum)

# Q.3)
# Ans.
factorial = 1
n = int(input("Enter a number:"))
for i in range(n, 0, -1):
    factorial = factorial*i
print(factorial)

# Q.4)
# Ans.
n = int(input("Enter a number:"))
print(f"The fcators of number {n} are: ")
for i in range(1, n+1):
    # Check if the entered number is divisible by each number counting upto entered number
    if n % i == 0:
        print(i, end=" ")

# Q.5)
# Ans.
i = 1  # Value initialized for  i only to process the loop
sum = 0
while i != 0:
    n = int(input("Enter a number:"))
    i = n
    sum += i  # Adding each number entered to sum
print(f"The total of the  numbers entered above is: {sum}")
