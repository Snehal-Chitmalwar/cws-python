# age = int(input("Enter your age="))
# if age > 14:
#     if age > 18:
#         print("Your are adult")
#     else:
#         print("Your are teenager")
# else:
#     print("Your are child")

num = int(input("Enter number:"))
if num >= 0:
    absolute = num
else:
    absolute = num*(-1)
print(f"The absolute numbers is {absolute}")

num = int(input("Enter a number = "))
print(f"Absolute number = {num*-1 if num<0 else num}")
