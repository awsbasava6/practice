# Division of Two Numbers - Simple Program

# Input from user
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

# Check if denominator is not zero
if num2 != 0:
    result = num1 / num2
    print("The result of division is:", result)
else:
    print("Error: Division by zero is not allowed.")

