"""
AND
A   B   R
F   F   F
F   T   F
T   F   F
T   T   T

OR
A   B   R
F   F   F
F   T   T
T   F   T
T   T   T

NOT (Reverses the Answer)

"""
physics = int(input("enter physics marks="))
chemistry = int(input("enter chemistry marks="))
print(physics > 33 and chemistry > 33)
print(physics > 33 or chemistry > 33)
print(not physics > 33)
