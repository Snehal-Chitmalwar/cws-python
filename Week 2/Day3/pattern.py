"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()

"""
11 12 13 14 15
11 12 13 14 15
11 12 13 14 15
11 12 13 14 15
11 12 13 14 15
"""
# for i in range(1, 6):
#     for j in range(11, 16):
#         print(j, end=" ")
#     print()

"""
10 20 30 40 50
10 20 30 40 50
10 20 30 40 50
10 20 30 40 50
10 20 30 40 50
"""
# for i in range(1, 6):
#     for j in range(1, 6):
#         j = j*10
#         print(j, end=" ")
#     print()


"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, end=" ")
#     print()


"""
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""
# for i in range(5, 0, -1):
#     for j in range(1, 6):
#         print(i, end=" ")
#     print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
