a = [23, 45, 34]
if 23 in a or 54 not in a:
    print("yes")
else:
    print("no")


"""
with_open
"""
# with open("hello.txt", "r") as f:
with open(mode="r", file="hello.txt") as f:
    data = f.read()
    print(data)
# print(f.read())
