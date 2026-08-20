temp = float(input("Enter your temperature: "))
unit = input("Enter the unit of temperature (C for  F to C, F for C to F): ")
if unit.upper() == "C" or unit.upper() == "c":
    celsius = round((temp -32) * 5/9, 2)
    print(f"{temp}°F is equal to {celsius}°C")
elif unit.upper() == "F" or unit.upper() == "f":
    fahrenheit = round((temp * 9/5) + 32, 2)
    print(f"{temp}°C is equal to {fahrenheit}°F")
else:
    print(f"{unit} is not a valid unit")