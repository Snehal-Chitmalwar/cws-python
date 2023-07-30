def checkPrime(num):
    count = 0
    for i in range(2, num+1):
        if num % i == 0:
            count += 1
    if count == 1:
        print(f"The number is prime")
    else:
        print(f"The number is not a prime")


checkPrime(4)
