# Q1. Make your own list of numbers. Ask a start and end position from User. Print the list from start position to end position using Slicing.
a = [1, 2, 3, 4, 3, 4, 4, 5, 6, 5, 8, 3, 3, 5]
start = int(input("Enter start position: "))
end = int(input("Enter end position: "))
print(a[start:end+1])

# Q2. Make your own list of numbers. Ask a start and end position from User. Make another different list which will contain number from start to end position. Use slicing logic.
my_list = [10, -5, 8, 3, -1, -9, 7, 2]
new_list = []
start = int(input("Enter start position: "))
end = int(input("Enter end position: "))
new_list = my_list[start:end+1].copy()
print(f"Result: {new_list}")

# Q3. Make your own list. Write a Python program that takes an integer as an input, and make a new list containing the last n elements of the original list. Using slicing logic.
my_list = [10, -5, 8, 3, -1, -9, 7, 2]
new_list = []
n = int(input("Enter a number: "))
new_list = my_list[-1:-n-1:-1].copy()
new_list.reverse()
print(f"Result: {new_list}")

# Q4. Make your own list. Write a Python program that takes an integer as an input, and make a new list containing the last n elements of the original list but in reverse order. Using slicing logic.
my_list1 = [10, -5, 8, 3, -1, -9, 7, 2]
new_list = []
n = int(input("Enter a number: "))
new_list = my_list1[-1:-n-1:-1].copy()
print(f"Result: {new_list}")
