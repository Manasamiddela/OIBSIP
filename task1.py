# Simple Calculator Program

# Taking first number from user
num1 = float(input("Enter first number: "))

# Taking second number from user
num2 = float(input("Enter second number: "))

# Asking user which operation to perform
operation = input("Enter operation (+, -, *, /): ")

# Performing calculation using if-else
if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error! Division by zero not allowed.")

else:
    print("Invalid operation entered.")