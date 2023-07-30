"""
file handling in python
different modes to open a file:
1. read(r,rb)
2. write(w,wb)
3. append(a,ab)
"""
f = open("word.docx", "rb")
data = f.read()
# data = f.readline()
# data = f.readlines()
print(data)
# print(f"The number of lines in your file is {len(data)}")

# print(data.count("o"))

f.close()
