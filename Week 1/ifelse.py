"""
if-else

syntax:

if condition:
    .....
    .....
elif condition:
    .....
    .....
else:
    .....
    .....
"""
# age = int(input("enter your age: "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Child")

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print(f"{num2} is equal to {num1}")

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# num4 = int(input("Enter 4th number: "))
# if (num1 > num2) and (num1 > num3) and (num1 > num4):
#     print(f"{num1} is greater")
# elif (num2 > num1) and (num2 > num3) and (num2 > num4):
#     print(f"{num2} is greater")
# elif (num3 > num1) and (num3 > num2) and (num3 > num4):
#     print(f"{num3} is greater")
# elif (num4 > num1) and (num4 > num2) and (num4 > num3):
#     print(f"{num4} is greater")

CustID = int(input("Enter the Customer ID:"))
CustName = input("Enter the Customer Name:")
Unit = int(input("Enter the Unit used:"))
if Unit <= 199:
    rate = 1.20
    bill = Unit*1.20
elif Unit >= 200 and Unit < 400:
    rate = 1.50
    bill = Unit*1.50
elif Unit >= 400 and Unit < 600:
    rate = 1.80
    bill = Unit*1.80
elif Unit >= 600:
    rate = 2.00
    bill = Unit*2.00

if bill < 100:
    print("Invalid Units used")
else:
    print(f"Amount Charges @Rs. {rate} per unit: ", bill)
    if bill > 400:
        surcharge = (0.15*bill)
        print(f"Surcharge Amount: {surcharge}")
        totalbill = (0.15*bill)+bill
    else:
        totalbill = bill
print(f"Net Amount paid by customer: {totalbill}")
