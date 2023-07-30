try:
    age = int(input("Enter age="))
    if age > 18:
        print("Adult")
    else:
        raise Exception("You are not adult")
except Exception as e:
    print("Some error occurred")
    print(f"Message -> {e}")
    pass
