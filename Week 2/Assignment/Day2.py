# Using for loop

# Q.1. Ask start and end number from user. Print all the numbers from start to end.
start = int(input("Enter start number:"))
end = int(input("Enter end number:"))
for i in range(start, end+1):
    print(i, end=" ")

# Q.2. Ask start and end number from user. Print all the numbers divisible by 5 or 7.
start = int(input("Enter start number:"))
end = int(input("Enter end number:"))
print(f"All the numbers divisible by 5 or 7 are:")
for i in range(start, end+1):
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")

# # Q.3. Ask start and end number from user. Print the sum of all the numbers divisible of 4.
start = int(input("Enter start number:"))
end = int(input("Enter end number:"))
sum = 0
for i in range(start, end+1):
    if i % 4 == 0:
        sum += i
print(
    f"The sum of all the numbers divisible by 4 from {start} to {end} is {sum}")

# # Q.4. Calculate the product/multiplication of numbers from 1 to 10.
mul = 1
for i in range(1, 11):
    mul *= i
print(f"The product of numbers from 1 to 10 is {mul}")

# # Q.5. Print the multiplication table of a number entered by user.
num = int(input("Enter a number: "))
for i in range(1, 11):
    product = num*i
    print(f"{num} * {i} = {product}")

# # Q.6. Count the total numbers divisible by 4 from 20 to 70
count = 0
for i in range(20, 71):
    if i % 4 == 0:
        count += 1
print(f"The total count of numbers divisible by 4 from 20 to 70 is {count}")

# # Q.7. Ask number from a user. Print if the number is prime or not.
num = int(input("Enter a number: "))
count = 0
for i in range(2, num+1):
    if num % i == 0:
        count += 1
if count == 1:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
