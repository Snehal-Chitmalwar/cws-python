# Q1. Write a Python program to read a text file and create a new file
#  with the same content but with all the words in uppercase.
f = open("AssignmentWeek7.txt", "r")
data = f.read().upper()
f.close()
new_f = open("NewFile.txt", "w")
new_f.write(data)
new_f.close()

# Q2. Write a Python program to read a text file and create a new file
# that contains the original lines in reverse order (i.e., the last line of
#  the original file should be the first line in the new file).
f = open("AssignmentWeek7.txt", "r")
data = f.readlines()
new_f = open("NewFile.txt", "a")
for i in range(len(data)-1, 0, -1):
    if i == len(data)-1:
        new_f.write(str(data[i])+"\n")
    else:
        new_f.write(str(data[i]))
f.close()
new_f.close()

# Q3. Write a Python program to read a text file and create a new file  with
# the same content, but with all vowels (a, e, i, o, and u)  replaced by an asterisk (*).
f = open("AssignmentWeek7.txt", "r")
data = f.read()
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
for i in vowels:
    if i in data:
        data = data.replace(i, "*")
f.close()
new_f = open("NewFile.txt", "w")
new_f.write(data)
new_f.close()

# Q4. Write a Python program to read two text files and create a new  file that
# contains the lines of the first file followed by the lines of the  second file
# (i.e., concatenate the two files).
f1 = open("AssignmentWeek7.txt", "r")
f2 = open("NewFile.txt", "r")
new_f = open("Concatenate.txt", "w")
new_f.write(f1.read()+"\n")
new_f.write(f2.read())
f1.close()
f2.close()
new_f.close()

# Q5. Write a Python program to read a text file and create a new file  with the
# same content, but with each word's first letter capitalized.
f = open("AssignmentWeek7.txt", "r")
new_f = open("NewFile.txt", "w")
for i in f.readlines():
    i = i.split()
    for j in i:
        new_f.write(j.capitalize()+" ")
    new_f.write("\n")
f.close()
new_f.close()

# Q6. Write a Python program to read a text file containing a list of  numbers
# (one per line) and create a new file with the same
f = open("AssignmentWeek7.txt", "r")
no_list = [int(i.strip()) for i in f.readlines()]
no_list.sort()
new_f = open("NewFile.txt", "a")
for i in no_list:
    new_f.write(str(i)+"\n")
f.close()
new_f.close()
