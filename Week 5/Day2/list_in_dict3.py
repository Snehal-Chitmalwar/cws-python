my_dict = {"Anirudh": [87, 67, 78, 78, 67,],
           "Sagar": [78, 67, 78, 56, 45],
           "xyz": [99, 78, 76, 45],
           "Akul": [89, 78, 78]
           }

another_dict = {}

for k, v in my_dict.items():
    another_dict[k] = v.copy()

my_dict["Anirudh"].clear()
print(my_dict)
print(another_dict)
