# Q1. Write a Python program that takes a user's input for a string and
# checks if the string is a palindrome. A palindrome is a word, phrase, number, or
#  other sequences of characters that reads the same forward and
# backward (ignoring spaces, punctuation, and capitalization). [6M]
string = input("Enter a string:").lower()
new_string = string.replace(" ", "")
reverselist = new_string[::-1]
print(new_string == reverselist)

# Q2. Write a Python program that takes a user's input for a list of integers
# and returns a new list containing only the unique elements from the original list,
# preserving the original order. [6M]
num = int(input("Enter the range for a list:"))
list1 = []
list2 = []
for i in range(num):
    element = int(input())
    list1.append(element)
for i in list1:
    if list2.count(i) < 1:
        list2.append(i)
print(list2)

# Q3. Write a Python program that takes a user's input for a positive
# integer (n) and prints all prime numbers up to n. [6M]
num = int(input("Enter a number:"))
count = 0
primelist = []
for i in range(2, num+1):
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
    if count == 1:
        primelist.append(i)
    count = 0
print(", ".join(str(k) for k in primelist))

# Q4. Write a Python program that takes a user's input for a string containing parentheses ( and ).
# Check whether the parentheses in the string are balanced or not.
# A string is balanced if the number of opening and closing parentheses match and every
# closing parenthesis has a corresponding opening parenthesis. [6M]
string = input()
print(string)
count1 = 0
count2 = 0
for i in string:
    if i == "(":
        count1 += 1
    elif i == ")":
        count2 += 1
if count1 != count2:
    print("False")
else:
    print("True")
