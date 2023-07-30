# Q1. Ask a string from a user. Then ask a letter from User. Just print YES or NO if that letter exists in that string.
string = input("Enter a string:")
letter = input("Enter a letter:")
flag = True
for i in range(0, len(string)):
    if letter.lower() == str(string[i]).lower():
        print("Yes")
        break
    else:
        flag = False
if flag == False:
    print("No")

# Q2. Ask a string from a user. Then ask a letter from User. Print the position of that letter in that string. If that letter does not exists, print INVALID LETTER.
string = input("Enter a string:")
letter = input("Enter a letter:")
count = 0
for i in range(0, len(string)):
    if letter.lower() == str(string[i]).lower():
        print(i)
        count += 1
if count == 0:
    print("INVALID LETTER")

# Q3. Ask 2 strings from a user. If both of the strings are digits, print
# the addition of both numbers, else print Invalid Numbers.
string1 = input("Enter a string 1:")
string2 = input("Enter a string 2:")
if string1.isdigit() == True and string2.isdigit() == True:
    sum = int(string1)+int(string2)
    print(sum)
else:
    print("INVALID NUMBERS")

# Q4. Write a code to check if the string is Mutable or Immutable.
string = "Good"
string[1] = "T"
if string == "Good":
    print("String is immutable")
else:
    print("String is mutable")
