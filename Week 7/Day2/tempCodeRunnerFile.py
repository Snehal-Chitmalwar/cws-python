with open(mode="r", file="hello.txt") as f:
    data = f.read()
    print(data)
print(f.read())