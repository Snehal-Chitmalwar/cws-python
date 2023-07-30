"""
Variables
Used to store data value
Rules:
    1. Should not start with number
    2. It can start with _ , a-z, A-Z
    3. It can contain numbers
    It is case sensitive

%d=integer
%f=float
%s=string(string,numbers)

"""

a = 5
b = 10
print(a)
print(b)
c = a+b
print(c)

name = "Snehal"
age = 24
gender = "female"
print("my name is", name)
print(f"my name is {name}")
print("my name is " + name)  # won't work with integers for concatenation
print("my name is %s" % (name))
print("my name is", name, end=" ")
print("my age is", age, end=" ")
print("my gender is", gender)
print(f"My name is {name}. My age is {age}. My gender is {gender}")
