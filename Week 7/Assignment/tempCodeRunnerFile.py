f = open("AssignmentWeek7.txt", "r")
no_list = [int(i.strip()) for i in f.readlines()]
no_list.sort()
new_f = open("NewFile.txt", "a")
for i in no_list:
    new_f.write(str(i)+"\n")
f.close()
new_f.close()