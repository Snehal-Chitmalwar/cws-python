file_name, n = input("Enter the file name you wish to collect details of:"), int(
    input("Enter a positive number:"))
f = open(file_name+".txt", "r")
data = f.readlines()
if n <= len(data):
    [print(data[i].strip()) for i in range(n)]
    # for i in range(n):
    #     print(data[i].strip())
else:
    print("The number of lines you have entered exceeds the number of lines in a file.")
    [print(i.strip()) for i in data]
    # for i in data:
    #     print(i.strip())
f.close()