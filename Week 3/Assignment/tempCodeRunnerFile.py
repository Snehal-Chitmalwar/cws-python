my_list = [10, -5, 8, 3, -1, -9, 7, 2]
new_list = []
n = int(input("Enter a number: "))
new_list = my_list[-1:-n-1:-1].copy()
new_list.reverse()
print(f"Result: {new_list}")