import logging

logging.basicConfig(level=logging.INFO)

def calculator():
    """
    the function create a simple calulator,
    using logging library we inform the user what kind of action will be performed and with what arguments,
    next we callculate and print the result with print() function
    """
    print("Give the operation using the correct number: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get the user's choice
    choice = input("Enter your choice (1/2/3/4): ")

    # Get the first number
    num1 = float(input("Enter the first number: "))

    # Get the second number
    num2 = float(input("Enter the second number: "))

    # Perform the selected operation
    if choice == '1':
        result = num1 + num2
        logging.info(f"I add {num1:.2f} and {num2:.2f}")
    elif choice == '2':
        result = num1 - num2
        logging.info(f"I subtract {num2:.2f} from {num1:.2f}")
    elif choice == '3':
        result = num1 * num2
        logging.info(f"I multiply {num1:.2f} by {num2:.2f}")
    elif choice == '4':
        if num2 == 0:
            logging.error("Division by zero is not allowed")
            return None
        result = num1 / num2
        logging.info(f"I divide {num1:.2f} by {num2:.2f}")
    else:
        logging.error("Invalid choice. Please select a valid option.")
        return None

    # Print the result
    print(f"The result is {result:.2f}")
    return result

result = calculator()