# count number of words in hello.txt
f = open("hello.txt", "r")
data = f.read()
print(f"The number of words in your file is {len(data.split())}")
f.close()

# replace all o to z while printing file
f = open("hello.txt", "r")
data = f.read()
newdata = data.replace("o", "z")
print(f"The data is {newdata}")
f.close()

# count no. of digits in file
f = open("hello.txt", "r")
# data = f.read()
count = 0
for i in f.read():
    # print(i)
    if i.isdigit():
        count += 1
print(count)
f.close()
