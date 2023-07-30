try:
    a = int(input("Enter number 1 = "))  # 10
    b = int(input("Enter number 2 = "))  # 5
    print(f"Your divide answer is {a/b}")
    print(C)
except ValueError:
    print("Please enter proper integer")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter proper numbers")
except Exception as e:
    print("Some unknown error occurred")
    print(f"Your error : {e}")
    print(f"Your error : {type(e).__name__}")
else:
    print("This is else")
finally:
    print("This is finally")
