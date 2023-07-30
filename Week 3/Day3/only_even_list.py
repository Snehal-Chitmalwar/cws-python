"""
there's a list A
put all even values of a in b
"""
a = [56, 43, 12, 65, 56, 56, 47, 0, 877, 65, 48, 99]
b = []
c = []
d = []
for i in range(0, len(a)):
    if a[i] % 2 == 0 and a[i] != 0:
        b.append(a[i])
    elif a[i] == 0:
        d.append(a[i])
    else:
        c.append(a[i])
print(b)
print(c)
print(d)
