range_category = int(
    input("Enter number of categoriies you want to add in a dictionary:"))
my_data = {}
for i in range(range_category):
    category = input("Enter the category:")
    values = []
    for j in range(4):
        value = input("Enter the value for category :")
        values.append(value)
    my_data[category] = values
item = input("Enter the item name you wish to search:")
for k, v in my_data.items():
    if v.count(item) > 0:
        print(k)
        break