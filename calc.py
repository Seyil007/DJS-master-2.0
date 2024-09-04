def calculator():
    operation = input("Enter operation (+, -, *, /): ")
    if operation not in ['+', '-', '*', '/']:
        return "Invalid operation"

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        return "Invalid input. Please enter numbers only."

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."

# Run the calculator
result = calculator()
print(result)
def calculator():
    operation = input("Enter operation (+, -, *, /): ")
    if operation not in ['+', '-', '*', '/']:
        return "Invalid operation"

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        return "Invalid input. Please enter numbers only."

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."

# Run the calculator
result = calculator()
print(result)
