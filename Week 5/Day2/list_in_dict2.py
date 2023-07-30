# my_dict = {"Anirudh": 45, "Sagar": 78, "Sanjay": 99, "Akul": 87}
my_dict = {"Anirudh": [87, 67, 78, 78, 67,],
           "Sagar": [78, 67, 78, 56, 45],
           "xyz": [99, 78, 76, 45],
           "Akul": [89, 78, 78]}
another_dict = my_dict.copy()
# list id will be same inside dictionary even if the dictionary is copied
print(id(my_dict["Anirudh"]))
print(id(another_dict["Anirudh"]))
