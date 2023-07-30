string1 = list(input("Enter 1st string:"))
string2 = list(input("Enter 2nd string:"))
j = 0
if len(string1) > len(string2):
    maximum, minimum = string1, string2
else:
    maximum, minimum = string2, string1
# newlist = list("".join(str(i) for i in maximum))
for i in range(0, len(maximum)):
    if i % 2 != 0:
        maximum.insert(i, minimum[j])
        j += 1
print("".join(str(i) for i in maximum))