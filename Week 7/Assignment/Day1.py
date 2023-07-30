# Q1.How many except statements can a try-except block have?
# c. more than 1

# Q2. What will be  o/p  of following code?
# def foo():
#     try:
#         return 1
#     finally:
#         return 2


# k = foo()
# print(k)
# ans: b.2

# Q3.
# def foo():
#     try:
#         print(1)
#     finally:
#         print(2)


# foo()
# ans= a.1 2

# Q4. Take i/p from user. Check if number is prime or not. If number is not prime,raise your own exception.Remember to handle all other exceptions.
try:
    num = int(input("Enter a number:"))
    count = 0
    for i in range(2, num+1):
        if num % i == 0:
            count += 1
    if count == 1:
        print("Prime")
    else:
        raise Exception("The number is not prime")
except Exception as e:
    print(f"The error occured is : {e}")
