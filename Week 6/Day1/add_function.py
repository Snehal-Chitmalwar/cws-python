def add():
    # local variables-x,y,z
    x = int(input("Enter number 1:"))
    y = int(input("Enter number 2:"))
    z = int(input("Enter number 3:"))
    print(x+y+z)


def mul():
    x = int(input("Enter number 1:"))
    y = int(input("Enter number 2:"))
    print(x*y)


add()
mul()


def my_function():
    my_list = []
    for i in range(5):
        num = int(input("Enter a number:"))
        my_list.append(num)
    print(my_list)


my_function()
