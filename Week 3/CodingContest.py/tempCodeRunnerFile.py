my_list = [45, 3, True, "CWS", 56, 89, "Hello", False, 78, 98]
for i in my_list:
    datatype = type(i)
    # print(datatype)
    if str(datatype) == "<class 'str'>":
        print(i)