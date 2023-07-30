a = "Good Morning Snehal"
count = 0
letter = input("Enter a letter:")
for i in range(0, len(a)):
    if letter.lower() == str(a[i]).lower():
        count += 1
print(f"The letter {letter} count is {count} times")
