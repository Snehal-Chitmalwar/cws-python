a = "Snehal chitmalwar"
# b = a.upper()
# print(b)
# b = a.lower()
# print(b)
# b = a.title()
# print(b)
# b = a.capitalize()  # if string starts with  number, then it won't work
# print(b)
# b = a.isupper()
# print(b)
# b = a.islower()
# print(b)
# b = a.isalpha()
# print(b)
# b = a.isalnum()
# print(b)
# b = a.isdigit()
# print(b)

string = input("Enter a string:")
if string.isalpha():
    print(string*3)
elif string.isdigit():
    print(int(string)**2)
else:
    print("Invalid")
