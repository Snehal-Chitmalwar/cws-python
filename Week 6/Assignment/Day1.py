# Q1. Write a Python function to find the Maximum and minimum of three numbers.
# Use 3 parameters.

def Find_Max_Min(num1, num2, num3):
    my_list = [num1, num2, num3]
    print(
        f"The maximum of above 3 numbers is {max(my_list)} and minimum is {min(my_list)}")


Find_Max_Min(2, 34, 23)

# Q2. Write a Python function to multiply all the numbers in a list.


def list_mul(my_list):
    mul = 1
    for i in my_list:
        mul = mul*i
    print(f"The multiplication of numbers in list is {mul}")


list_mul([2, 4, 10])

# Q3. Ask a number from user. Pass that number as a parameter to a function.
# Check if the number is prime or not.


def isPrime(num):
    count = 0
    for i in range(2, num+1):
        if num % i == 0:
            count += 1
    if count == 1:
        print("The number is Prime")
    else:
        print("The number is not a Prime")


num = int(input("Enter the number:"))
isPrime(num)

# Q4. Write a Python program to reverse a string.


def str_Reverse(str):
    print(str[::-1])


str_Reverse("Snehal")

# Q5. Write a Python function that checks whether a passed string is palindrome or not.


def str_isPalindrome(str):
    if str.lower() == str[::-1].lower():
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")


str_isPalindrome("Mom")

# Q6. Write a Python function to create and print a list where the values
# are square of numbers between 1 and 30 (both included).


def list_square(start, end):
    my_list = []
    for i in range(start, end+1):
        my_list.append(i**2)
    print(my_list)


list_square(1, 30)

# Q7. Write a function that inputs a number and prints the
#  multiplication table of that number


def getTable(num):
    for i in range(1, 11):
        print(f"{num}*{i} = {num*i}")
    print()


getTable(2)

# Q8. Write a function prodDigits() that inputs a number and
# prints the product of digits of that number.


def prodDigits(num):
    my_list = list(str(num))
    product = 1
    for i in my_list:
        product = product*int(i)
    print(f"The product of digits is {product}")


prodDigits(23)
