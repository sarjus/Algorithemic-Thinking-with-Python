"""
This program performs basic arithmetic operations (addition, subtraction, multiplication, division, 
    modulus, and a combined operation) on user input numbers.

    Operations included:
    1. Addition: num1 + num2
    2. Subtraction: num1 - num2
    3. Multiplication: num1 * num2
    4. Division: num1 / num2
    5. Modulus: num1 % num2
    Author : Sarju S
    Date: 08-10-2024
"""
# Get user input
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))
num3 = float(input("Enter the third number (num3): "))

# Addition
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_result}")

# Subtraction
diff_result = num1 - num2
print(f"The difference when {num2} is subtracted from {num1} is: {diff_result}")

# Multiplication
prod_result = num1 * num2
print(f"The product of {num1} and {num2} is: {prod_result}")

# Division
quotient_result = num1 / num2
print(f"The quotient when {num1} is divided by {num2} is: {quotient_result}")

# Modulus
remainder_result = num1 % num2
print(f"The remainder when {num1} is divided by {num2} is: {remainder_result}")
