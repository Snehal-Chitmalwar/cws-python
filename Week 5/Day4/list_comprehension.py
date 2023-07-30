# List comprehension
import datetime

# 1 to 100000000
# a = []

start_time = datetime.datetime.now()

# for i in range(1, 100000000):
#     a.append(i)
a = [i for i in range(1, 100000000)]

end_time = datetime.datetime.now()
print(end_time-start_time)
