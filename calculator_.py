sembol = input("What is your process(-,+,/,*)? ")

if sembol == "-":
    x = int(input("Enter your 1st number: "))
    y = int(input("Enter your 2nd number: "))
    a = x - y
    print(f"result: {a}")
elif sembol == "+":
    x = int(input("Enter your 1st number:"))
    y = int(input("Enter your 2nd number: "))
    a = x + y
    print(f"result: {a}")
elif sembol == "*":
    x = int(input("Enter your 1st number:"))
    y = int(input("Enter your 2nd number: "))
    a = x * y
    print(f"result: {a}")
elif sembol == "/":
    x = int(input("Enter your 1st number:"))
    y = int(input("Enter your 2nd number: "))
    a = x / y
    print(f"result: {a:.2f}")
