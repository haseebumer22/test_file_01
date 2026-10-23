
def calculator(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    print("\n--- Calculator Results ---")
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)


# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the function
calculator(num1, num2)
