import os
import time
from datetime import date, timedelta

print("WELCOME TO FILE SIZE ANALYZER")
file_path = input(
    "Enter the file name or directory path you wish to analyze utilization for:")
report_file = input(
    "Enter the file name where you want to generate the utilization report:")
# report_format = input(
#     "Enter the format in which you wish to generate the utilization report:")
print("Please select the search criteria for analyzing file:")
file_size_criteria = input("Enter the criteria for file size in MB:")
modification_date = int(input("Enter the span of days for date criteria :"))
today_date = date.today().isoformat()
# print(today_date)
n_days_before = (date.today()-timedelta(days=modification_date)).isoformat()
# print(n_days_before<today_date)
size = file_size_criteria.split()
file_list = []
file_size = []
file_modified_date = []
for path in os.listdir(file_path):
    if os.path.isfile(os.path.join(file_path, path)):
        file_list.append(path)
        file_size.append(os.stat(os.path.join(file_path, path)).st_size)
        file_modified_date.append(time.strftime(
            '%Y-%m-%d', time.localtime(os.path.getmtime(os.path.join(file_path, path)))))
print(file_modified_date)