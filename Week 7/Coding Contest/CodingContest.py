# Q1. Write a Python program that takes a user's input for a file name  and reads
#  the content of the file. The program should print the  total number of lines,
#  words, and characters in the file.
file_name = input("Enter the file name you wish to collect details of:")
f = open(file_name+".txt", "r")
data = f.readlines()
character_list = []
[[character_list.append(
    len(j)) for j in i.strip().split()] for i in data]
words_list = [len(i.split()) for i in data]
print(
    f"Lines: {len(data)}, Words: {sum(words_list)}, Characters: {sum(character_list)}")
f.close()

# Q2. Write a Python program that takes a user's input for a file  name and a
# positive integer (n). The program should read the  content of the file and
# print the first n lines.
file_name, n = input("Enter the file name you wish to collect details of:"), int(
    input("Enter a positive number:"))
f = open(file_name+".txt", "r")
data = f.readlines()
if n <= len(data):
    [print(data[i].strip()) for i in range(n)]
else:
    print("The number of lines you have entered exceeds the number of lines in a file.")
    [print(i.strip()) for i in data]
f.close()

# Q3. Write a Python program that takes a user's input for a file  name and
# reads the content of the file. The program should print a  dictionary with
# line numbers as keys and the lines as values.
file_name = input("Enter the file name you wish to collect details of:")
f = open(file_name+".txt", "r")
my_dict, data = {}, f.readlines()
for i in range(len(data)):
    my_dict[i+1] = data[i].strip()
print(my_dict)

# Q4. Write a Python program that takes a user's input for a file  name and
# tries to read the content of the file. If the file does not  exist, print
# an error message using exception handling.
file_name = input("Enter the file name you wish to collect details of:")
try:
    f = open(file_name+".txt", "r")
except FileNotFoundError:
    print("Error occured: File you're trying to read does not exist.")
except Exception as e:
    print("Some error occured: {e}")

# Q5. Write a Python program that takes a user's input for a file  name
# and a word. The program should read the content of the file  and find the
# line number where the given word first appears. If the  word is not found in the
#  file, print a message indicating this. Use  exception handling to deal
#  with non-existent files.
file_name, word = input("Enter the file name you wish to collect details of:"), input(
    "Enter a word you wish to search in file:")
try:
    f = open(file_name+".txt", "r")
    data = f.readlines()
    for i in range(0, len(data)):
        if word.lower() in str(data[i].strip()).lower():
            print(f"The word \"{word}\" first appears on line {i+1}")
            break
except FileNotFoundError:
    print("Error occured: File you're trying to read does not exist.")
except Exception as e:
    print("Some error occured: {e}")

# Q6. Write a Python program that takes a user's input for a file  name
# and a positive integer (n). The program should read the  content of the
#  file and print the nth line. If the file has fewer lines  than the input
#  integer, print a message indicating this. Use  exception handling to deal
# with non-existent files and invalid  inputs.
file_name, n = input("Enter the file name you wish to collect details of:"), int(
    input("Enter a positive number:"))
try:
    f = open(file_name+".txt", "r")
    data = f.readlines()
    if n > 0 and n <= len(data):
        print(f"Line {n}: {data[n-1].strip()}")
    elif n > 0 and n > len(data):
        print("Sorry!! The line you wish to read from the file do not exist")
    else:
        raise Exception("Input you have entered is Invalid.")
except FileNotFoundError:
    print("Error occured: File you're trying to read does not exist.")
except Exception as e:
    print(f"Some error occured: {e}")
