name = "noon"
name1 = name[-1::-1]
if name.lower() == name1.lower():
    print(f"The word {name} is a palindrome")
else:
    print(f"The word {name} is not a palindrome")
