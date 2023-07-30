string = input("Enter a string:")
if string.isalpha():
    print(string*3)
elif string.isdigit():
    print(int(string)**2)
else:
    print("Invalid")