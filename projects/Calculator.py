def add(x, y):
    "Calculate and return the sum of two numbers."
    return x + y

def subtract(x, y):
    "Calculate and return the difference between two numbers."
    return x - y

def multiply(x, y):
    "Calculate and return the product of two numbers."
    return x * y

def divide(x, y):
    "Calculate and return the quotient of two numbers, checking for division by zero."
    if y == 0:
        return "Error: Division by zero"
    return x / y

def display_menu():
    "Display the available operations for the calculator to the user."
    print("\nWelcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

def get_numbers():
    "Prompt the user to input two numbers and return them as floats."
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def main():
    "Main function that controls the flow of the calculator program."
    while True:
        display_menu()  # Show the available operations
        
        operation = input("Enter the operation (1, 2, 3, or 4) or 'q' to quit: ")

        if operation.lower() == 'q':
            print("Thank you for utilizing the calculator. Have a great day!")
            break

        if operation not in ['1', '2', '3', '4']:
            print("Invalid output! Please select a valid operation (1, 2, 3, or 4).")
            continue  # Restart the loop for a new operation input

        num1, num2 = get_numbers()

        if operation == '1':
            result = add(num1, num2)
            print(f"\nThe result of {num1} + {num2} = {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"\nThe result of {num1} - {num2} = {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"\nThe result of {num1} * {num2} = {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"\nThe result of {num1} / {num2} = {result}")

        print("\n->If you want to perform another calculation, please respond with 'yes'.")
        print("->If you want to exit, respond with 'no'.")

        continue_calculation = input("->Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_calculation != 'yes':
            print("'Thank you for utilizing the calculator. Have a great day!'")
            break

if __name__ == "__main__":

    main()
