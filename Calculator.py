operator = input("Enter an operator (+, -, *, /): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# print("You entered:", num1, operator, num2)
if operator == "+":
    result = round(num1 + num2, 2)
    sample = "Sum"
elif operator == "-":
    result = round(num1 - num2, 2)
    sample = "Difference"
elif operator == "*":
    result = round(num1 * num2, 2)
    sample = "Product"
elif operator == "/":
    result = round(num1 /num2, 2)
    sample = "Quotient"
elif operator == "%":
    result = round(num1 % num2, 2)
    sample = "Remainder"
else:
    print("Invalid operator")
    result = None
    sample = "None"

print(f"The {sample} of the {num1} and {num2} is: {result}")
