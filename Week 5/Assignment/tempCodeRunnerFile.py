my_dict = {"John": [89, 56, 78, 56, 45], "Tom": [78, 56, 45, 34, 34], "James": [
    45, 89, 90, 67, 56], "Rose": [45, 89, 67, 78, 67], "Jasmine": [90, 89, 78, 67, 56]}
for k, v in my_dict.items():
    print(f"The highest marks of {k} is {max(v)}")
print()