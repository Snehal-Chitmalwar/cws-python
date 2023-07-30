# Q1. Write a program to create a list of unique characters from a given string and print the list.
string = input("Enter a string:")
print(f"List of unique characters: {list(string)}")

# Q2. Write a program to find the common elements between two strings and print the common characters as a list.
string1 = input("Enter 1st string:")
string2 = input("Enter 2nd string:")
listcommon = []
for i in string1:
    if string2.count(i) > 0 and listcommon.count(i) == 0:
        listcommon.append(i)
print(f"List of common characters: {listcommon}")

# Q3. Write a program to find the union, intersection of two different sets.
set1 = {23, 56, 78, 67}
set2 = {56, 78, 67, 56, 89}
print(set1.intersection(set2), set1.union(set2))

# Q4. Write a program to remove all the duplicate words from a
# given string and print the resulting string.
string = input("Enter a string:").split()
new_string = ""
for i in string:
    if (new_string.count(i) < 1) or i == ".":
        new_string += (i+" ")
print(new_string)

# Q5. Write a program to create a list of characters from a given
# string, reverse the order of the characters in the list, and then
# convert the list back to a string and print it.
string = list(input("Enter a string:"))
string.reverse()
print("".join(str(i) for i in string))

# Q6. Write a program that takes two strings as input, creates lists of
# their characters, then prints a new string formed by taking
# characters alternately from the input strings. If one string is shorter
# than the other, append the remaining characters from the longer
# string to the result. (HARD)
string1 = list(input("Enter 1st string:"))
string2 = list(input("Enter 2nd string:"))
j = 0
if len(string1) > len(string2):
    maximum, minimum = string1, string2
else:
    maximum, minimum = string2, string1
for i in range(0, len(maximum)):
    if i % 2 != 0:
        maximum.insert(i, minimum[j])
        j += 1
print("".join(str(i) for i in maximum))
