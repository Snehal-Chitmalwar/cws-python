my_dict = {"Anirudh": [87, 67, 78, 78, 67,],
           "Sagar": [78, 67, 78, 56, 45],
           "xyz": [99, 78, 76, 45],
           "Akul": [89, 78, 78]}
sum = 0
for k, v in my_dict.items():
    for j in v:
        sum += j
    print(f"{k} - {sum}")
    sum = 0
# or
for k, v in my_dict.items():
    print(f"{k} - {sum(v)}")
