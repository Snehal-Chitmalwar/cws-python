# Using while loop

# Q.1. Ask start and end number from user. Print all the numbers from start to end.
start = int(input("Enter start number:"))
end = int(input("Enter end number:"))
while start <= end:
    print(start, end=" ")
    start += 1

# Q.2. Ask start and end number from user. Print all the numbers divisible by 5 or 7.
start = int(input("Enter start number:"))
end = int(input("Enter end number:"))
print(f"All the numbers divisible by 5 or 7 are:")
while start <= end:
    if (start % 5 == 0) or (start % 7 == 0):
        print(start, end=" ")
    start = start+1

# Q.3. Ask start and end number from user. Print the sum of all the numbers divisible of 4.
start = int(input("Enter start number:"))
end = int(input("Enter end number:"))
sum = 0
while start <= end:
    if start % 4 == 0:
        sum = sum+start
    start += 1
print(
    f"The sum of all the numbers divisible by 4 from {start} to {end} is {sum}")

# Q.4. Calculate the product/multiplication of numbers from 1 to 10.
i = 1
mul = 1
while i <= 10:
    mul = mul*i
    i += 1
print(f"The product of numbers from 1 to 10 is {mul}")

# Q.5. Print the multiplication table of a number entered by user.
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    product = num*i
    print(f"{num} * {i} = {product}")
    i += 1

# Q.6. Count the total numbers divisible by 4 from 20 to 70
i = 20
count = 0
while i <= 70:
    if i % 4 == 0:
        count += 1
    i += 1
print(f"The total count of numbers divisible by 4 from 20 to 70 is {count}")

# Q.7. Ask number from a user. Print if the number is prime or not.
num = int(input("Enter a number: "))
i = 2
count = 0
while i <= num:
    if num % i == 0:
        count += 1
    i += 1
if count == 1:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
