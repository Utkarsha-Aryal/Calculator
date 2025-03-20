def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."

# Example usage:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Result:", divide(num1, num2))
