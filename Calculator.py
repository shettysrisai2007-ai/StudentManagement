
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b


def calculator():
    print("===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    while True:
        choice = input("\nEnter your choice (1-7): ")

        if choice == "7":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice! Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(a, b))

            elif choice == "2":
                print("Result:", subtract(a, b))

            elif choice == "3":
                print("Result:", multiply(a, b))

            elif choice == "4":
                print("Result:", divide(a, b))

            elif choice == "5":
                print("Result:", modulus(a, b))

            elif choice == "6":
                print("Result:", power(a, b))

        except ValueError:
            print("Please enter valid numbers!")


calculator()
