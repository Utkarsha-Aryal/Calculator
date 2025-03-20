from Addition import Addition
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("\nEnter your choice (1-4): ")

    if choice == '1':
        result = Addition(a, b).add_numbers()
        print(f"Result: {result}")
    elif choice == '2':
        result = Subtraction(a, b).subtract_numbers()
        print(f"Result: {result}")
    elif choice == '3':
        result = Multiplication(a, b).multiply_numbers()
        print(f"Result: {result}")
    elif choice == '4':
        result = Division(a, b).divide_numbers()
        print(f"Result: {result}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
