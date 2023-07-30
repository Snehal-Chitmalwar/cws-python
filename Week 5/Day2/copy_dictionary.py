my_dict = {"Anirudh": 45, "Sagar": 78, "Sanjay": 99, "Akul": 87}

another_dict = my_dict.copy()
# using copy function will not make changes in both dictionaries
print(id(my_dict))
print(id(another_dict))
