# Q.1.
# Ans:
num = int(input("Enter the number: "))
if num < 0:
    print(f"{num} is a negative number.")
else:
    if num == 0:
        print(f"{num} is neither positive nor negative")
    else:
        print(f"{num} is a positive number.")

# Q.2.
# Ans:
num = int(input("Enter the number: "))
if num % 2 == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")

# Q.3.
# Ans:
num = int(input("Enter the number between 1 to 7: "))
# n1,n2,n3,n4,n5,n6,n7="Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
if num == 1:
    day = "Monday"
elif num == 2:
    day = "Tuesday"
elif num == 3:
    day = "Wednesday"
elif num == 4:
    day = "Thursday"
elif num == 5:
    day = "Friday"
elif num == 6:
    day = "Saturday"
elif num == 7:
    day = "Sunday"
else:
    print(f"Please enter valid number between 1 to 7 only.")
if num >= 1 and num <= 7:
    print(f"It is {day}")

# Q.4.
# Ans:
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i = i+1

# Q.5.
# Ans:
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# temp = num2
# num2 = num1
# num1 = temp
# print(f"The value of number 1 after swapping is: {num1}")
# print(f"The value of number 2 after swapping is: {num2}")
