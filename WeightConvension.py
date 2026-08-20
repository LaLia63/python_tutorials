conversion = input("Enter conversion type (1 =kg to lb or 2 = lb to kg): ")
if conversion == "1":
    kg = float(input("Enter weight in kilograms: "))
    lb = round(kg * 2.20462, 2)
    print(f"{kg}kg is equal to {lb} lb")
elif conversion == "2":
    lb = float(input("Enter weight in pounds: "))
    kg = round(lb / 2.20462, 2)
    print(f"{lb}lb is equal to {kg} kg")
else:
    print(f"{conversion} was not valid")