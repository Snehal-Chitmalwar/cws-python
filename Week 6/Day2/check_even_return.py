def checkEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


r = checkEven(10)
if r == True:
    print("Even")
else:
    print("Odd")
