# Simple Calculator
# This program performs basic arithmetic operations.

try:
    # Take two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display available operations
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take the user's choice
    choice = input("Enter your choice (1-4): ")

    # Perform the selected operation
    if choice == "1":
        print("Result =", num1 + num2)

    elif choice == "2":
        print("Result =", num1 - num2)

    elif choice == "3":
        print("Result =", num1 * num2)

    elif choice == "4":
        # Check for division by zero
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        print("Result =", num1 / num2)

    else:
        print("Invalid choice.")

# Handle invalid number input
except ValueError:
    print("Invalid input. Please enter numbers only.")

# Handle division by zero
except ZeroDivisionError as e:
    print("Error:", e)