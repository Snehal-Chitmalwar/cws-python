# a = "Good morning CWS. Ok bye"
# print(a)
# b = a.replace("o", "z")
# print(b)

sentence = input("Enter a sentence:")
letter = input("Enter a letter to be replaced:")
new_letter = input("Enter new letter:")
new_sentence = sentence.replace(letter, new_letter)
print(new_sentence)
