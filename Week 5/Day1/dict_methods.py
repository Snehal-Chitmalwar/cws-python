a = {"Anirudh": 45, "Sagar": 78, "Sanjay": 99, "Akul": 87}
# print(a.get("Anirudh"))
# print(a.get("Anirudhh"))

# check if key exists
# b = "Anirudhg"
# if a.get(b) != None:
#     print("Exists")
# else:
#     print("Does not Exists")

# update single/multiple updates
# a.update({"Anirudh": 67})
# print(a)

# enter student name
name = input("Enter student's name:")
if a.get(name) != None:
    if a.get(name) > 33:
        print("Pass")
    else:
        print("Fail")
else:
    print("Student donot exists")
