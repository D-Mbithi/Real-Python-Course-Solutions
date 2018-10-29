while True:
    try:
        user = int(input("Enter an integer: "))
        print(f"Your integer is {user}")
        break
    except ValueError:
        print("Try again.")
