a = [45, 31, 56, 78, 66, 45, 77, 12, 65]
# b = [i+5 if i % 2 == 0 else i-5 for i in a]
b = [i+5 if i % 2 == 0 else i-5 for i in a if i > 100]
print(b)


#
a = ["Anirudh", "Sagar", "Aeroplane", "Elephant", "Good"]
b = [i for i in a if i.count("o") > 0]
print(b)

c = "Snehal"
print("n" in c)
