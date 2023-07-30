a = {"Anirudh": 45, "Sagar": 78, "Sanjay": 99, "Akul": 87}
print(a)
a["Sagar"] = 100
a["xys"] = 90
print(a)

# ask input for 5 students n print dictionary
a = {}
for i in range(5):
    k = input("Enter student name=")
    v = int(input("Enter student marks= "))
    a[k] = v
print(a)
