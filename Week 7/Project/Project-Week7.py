# import Python modules
import os
import time
from datetime import date, timedelta

print("WELCOME TO FILE SIZE ANALYZER")

# input the file path/directory
file_path = input(
    "Enter the file name or directory path you wish to analyze utilization for:")

# input the out file path with extension
report_file = input(
    "Enter the file name where you want to generate the utilization report:")

# input the search criteria
print("Please select the search criteria for analyzing file:")

# input size criteria as: greater than x MB or lower than x MB or equal to x MB
file_size_criteria = input("Enter the criteria for file size in MB:")
size = file_size_criteria.split()

# input last number of days in which you want to search for files
modification_date = int(input("Enter the span of days for date criteria :"))
n_days_before = (date.today()-timedelta(days=modification_date)).isoformat()

# initialize lists to store file names, size and modified dates
file_list = []
file_size = []
file_modified_date = []

# store the respective details in respective list using functions from OS module
for path in os.listdir(file_path):
    if os.path.isfile(os.path.join(file_path, path)):
        file_list.append(path)
        file_size.append(os.stat(os.path.join(file_path, path)).st_size)
        file_modified_date.append(time.strftime(
            '%Y-%m-%d', time.localtime(os.path.getmtime(os.path.join(file_path, path)))))

count = 0
total_size = 0.0

# create a target file to enter report
f = open(report_file, "a")
f.write("| File Name | Size | Type | Date |\n")
for i in range(0, len(file_list)):
    # to store extension of files in a directory
    type_file = file_list[i].split(".")
    # convert bytes to MB
    each_file_size = format(round(file_size[i]/(1024*1024), 3))

    # search criteria-- greater than x MB
    if (("greater" in file_size_criteria.lower() or ">" in file_size_criteria.lower()) and
            (each_file_size > size[2])) and (n_days_before <= file_modified_date[i]):
        f.write("| "+file_list[i]+" | " + each_file_size +
                "MB | "+type_file[1].upper()+" | "+file_modified_date[i]+" |")
        f.write("\n")
        # calculate total count of files based on search criteria
        count += 1
        # calculate total size based on search criteria
        total_size += float(each_file_size)

     # search criteria-- lower than x MB
    elif (("lower" in file_size_criteria.lower() or "<" in file_size_criteria.lower()) and
          (each_file_size < size[2])) and (n_days_before <= file_modified_date[i]):
        f.write("| "+file_list[i]+" | " + each_file_size +
                "MB | "+type_file[1].upper()+" | "+file_modified_date[i]+" |")
        f.write("\n")
        # calculate total count of files based on search criteria
        count += 1
        # calculate total size based on search criteria
        total_size += float(each_file_size)

     # search criteria-- equal to x MB
    elif (("equal" in file_size_criteria.lower() or "=" in file_size_criteria.lower()) and
          (each_file_size == size[2])) and (n_days_before <= file_modified_date[i]):
        f.write("| "+file_list[i]+" | " + each_file_size +
                "MB | "+type_file[1].upper()+" | "+file_modified_date[i]+" |")
        f.write("\n")
        # calculate total count of files based on search criteria
        count += 1
        # calculate total size based on search criteria
        total_size += float(each_file_size)
# print total no. of files
f.write(f"Total Files: {count}\n")
# print total size of files
f.write(f"Total Size: {total_size}MB")
