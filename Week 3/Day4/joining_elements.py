a = (54, 85, 74, 10, -55, 62, 99, 56, 56, 56)
# 45 | 54 | ...... 45

# for i in a:
#     print(i,end=" | ")


print(" | ".join(str(i) for i in a))
print([i+5] for i in a)
