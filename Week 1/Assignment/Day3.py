# Q.1.Python program to add 2 numbers entered by User
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
sum = num1+num2
print(f"The sum for 2 numbers is {sum}")

# Q.2.Python program to convert kilometers to miles. Ask kilometer from user
km = float(input("Enter KMs covered by you:"))
miles = km*0.621371
print(f"Uh have covered {miles} miles.")

# Q.3.Ask 3 numbers from user n calculate the average
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
avg = (num1+num2+num3)/3
print(f"The average for above 3 numbers is {avg}")

# Q.4.Ask value in rupees and convert into paise
rupees = int(input("Enter rupees:"))
paise = rupees*100
print(f"{rupees} rupees is {paise} paise")

# Q.5.Calculate area of square by taking side from user
side = float(input("Enter side of a square: "))
area = side*side
print(f"The area of square with side {side} is {area}")

# Q.6.Ask number of games played in a tournament.Ask user number of games won and number of games loss. Calculate number of tie and total points
# (1win=4 points, 1tie=2 points)
Gamesplayed = int(input("Enter total number of games played: "))
Gameswon = int(input("Enter total number of games won: "))
Gameslost = int(input("Enter total number of games lost: "))
NoOfTie = Gamesplayed-(Gameswon+Gameslost)
totalpoints = Gameswon*4+NoOfTie*2
print(f"The total number of ties are {NoOfTie}")
print(f"The total number of points achieved are {totalpoints}")
