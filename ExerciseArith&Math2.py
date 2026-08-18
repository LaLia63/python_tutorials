import math
# C = square root of (a^2 + b^2) # equation for hypotenuse of a right triangle

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of the hypotenuse is: {round(c, 2)}cm")
