# write mode->overrides the file

f = open("hey.txt", "w")
name = input("Enter your name:")
age = int(input("Enter your age:"))
gender = input("Enter your gender:")
f.write(f"Your name is {name}\n")
f.write(f"Your age is {age}\n")
f.write(f"Your gender is {gender}")

# f.write("hello world\n")
# f.write("my hobby is sketching\n")
f.close()
report = ['File1.txt', 'New Microsoft PowerPoint Presentation.pptx',
          'Week7-CodingContest_SnehalChitmalwar.pdf']
type_file = report[0].split(".")
print(type_file)
