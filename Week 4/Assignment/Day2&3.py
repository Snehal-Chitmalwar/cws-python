# Q1. Ask a sentence from the user. Count the number of words in a sentence using split() method
sentence = input("Enter a sentence:")
words = sentence.split()
print(f"The total number of words in a sentence are:{len(words)}")

# Q2. Ask a sentence from the user. Count the number of vowels in that sentence.
sentence = (input("Enter a sentence:").lower())
count = 0
for i in range(len(sentence)):
    if str(sentence[i]) == "a" or str(sentence[i]) == 'e' or str(sentence[i]) == 'i' or str(sentence[i]) == 'o' or str(sentence[i]) == 'u':
        count += 1
print(count)

# Q3. Write a program to find the longest word in a given string and print the word.
sentence = input("Enter a sentence:").split()
for i in range(len(sentence)-1):
    if len(sentence[i]) > len(sentence[i+1]):
        maximum = sentence[i]
    else:
        maximum = sentence[i+1]
print(f"The largest word of the sentence is: {maximum}")

# Q4. Write a program to find the shortest word in a given string and print the word. Make sure that all the words are of different length in the string.
sentence = input("Enter a sentence:").split()
for i in range(len(sentence)-1):
    if len(sentence[i]) < len(sentence[i+1]):
        minimum = sentence[i]
    else:
        minimum = sentence[i+1]
print(f"The shortest word of the sentence is: {minimum}")

# Q5. Write a program to create a new string by swapping the first and last characters of a given string. If the string has only one character, print the original string.
string = input("Enter a string:")
if len(string) == 1:
    print(string)
else:
    print(string[-1:-2:-1]+string[1:len(string)-1]+string[0:1])

# Q6. Write a program to remove all spaces from a given string and print the resulting string.
string = input("Enter a string:").split()
new_string = ""
for i in range(len(string)):
    new_string += string[i]
print(new_string)

# Q7. Write a program to concatenate two given strings without using the + operator and print the result. (Hint: Store 2 strings in list, and print using join method)
string = input("Enter a string:").split()
print("".join(str(i) for i in string))

# Q8. Write a program that takes a string as input and prints the string with its first letter capitalized and the rest of the string in lowercase.
string = input("Enter a string:")
print(string[0].capitalize()+string[1::])

# Q9. Write a program to check if a given string contains any digits
# and print "Contains digits" if it does, otherwise print "Does not
# contain digits".
string = input("Enter a string:")
if string.isalpha():
    print(f"Does not Contains digits")
elif string.isalnum():
    print(f"Contains digits")

# Q10. Write a program to replace all the spaces with “-” character.
# Use replace() method.
string = input("Enter a string:")
print(string.replace(" ", "-"))

# Q11. Ask a sentence from user. Then ask a letter from user. Remove
# all the letter from the sentence entered by user and print the result.
sentence = input("Enter a sentence:")
letter = input("Enter a letter:")
new_sentence = sentence.replace(letter, "")
print(new_sentence.replace("  ", " "))
