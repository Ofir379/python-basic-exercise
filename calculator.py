import sys

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
    except ZeroDivisionError:
        return "Error: Division by zero"
    return result

def calculator():
    if len(sys.argv) < 4:
        print("Usage: python3 calculator.py num1 num2 [num3 ...] operation")
        sys.exit(1)

    *number_args, operation = sys.argv[1:]

    try:
        numbers = [float(arg) for arg in number_args]
    except ValueError:
        print("Error: All inputs before the operation must be numbers.")
        sys.exit(1)

    if operation == "add":
        result = add(numbers)
    elif operation == "subtract":
        result = subtract(numbers)
    elif operation == "multiply":
        result = multiply(numbers)
    elif operation == "divide":
        result = divide(numbers)
    else:
        print("Error: Unsupported operation. Use add, subtract, multiply, or divide.")
        sys.exit(1)

    print("Result:", result)

if __name__== "__main__":
    calculator()



