"""
Q1. Print the following patterns
a.
    *
    * *
    * * *
    * * * *
    * * * * *
"""
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

"""
b. 1 2 3 4 5
   1 2 3 4
   1 2 3
   1 2
   1
"""
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

"""
c.  1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
"""
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

"""
d.  1
    3 5
    7 9 11
    13 15 17 19
    21 23 25 27 29
"""
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()

"""
e.  1 2 1 2 1
    1 2 1 2 1
    1 2 1 2 1
    1 2 1 2 1
    1 2 1 2 1
"""
for i in range(1, 6):
    for j in range(1, 6):
        if j % 2 != 0:
            print("1", end=" ")
        else:
            print("2", end=" ")
    print()

"""
f.  *
    * *
    * * *
    * * * *
    * * * * *
"""
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

"""
g.      1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
"""
for i in range(1, 6):
    for j in range(i, 5):
        # for j in range(5,i,-1):
        print(" ", end=" ")
    for k in range(i):
        print(i, end=" ")
    print()
