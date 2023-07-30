# Q1.SUM OF ALL NUMBERS IN A TEXT FILE
f = open("AssignmentWeek7.txt", "r")
my_list = []
[my_list.append(int(i.strip())) for i in f.readlines()]
print(sum(my_list))

# Q2.WORD EXIST  IN FILE OR NOT
word = input("Enter any word:").lower()
f = open("AssignmentWeek7.txt", "r")
print("Yes") if word in f.read().lower() else print("No")

# Q3. FREQUENCY OF WORDS IN A FILE
word = input("Enter any word:").lower()
f = open("AssignmentWeek7.txt", "r")
print(f"The frequency of word in the file is {f.read().lower().count(word)}")

# Q4. REVERSE ORDER
f = open("AssignmentWeek7.txt", "r")
for i in f.readlines():
    i = i.split()
    for j in i:
        print(j[::-1], end=" ")
    print()

# Q5. PRINT LINES CONTAINING "a"
f = open("AssignmentWeek7.txt", "r")
[print(i) for i in f.readlines() if "a" in i.lower()]
