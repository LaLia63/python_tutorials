# collection = single "variable" used to store multiple values
# list      = [] ordered and changeable. Duplicates OK
# Set     = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple  = () ordered and unchangeable. Duplicates OK. FASTER

cars = ["BMW", "Lambo", "Toyota", "Suzuki","Honda"]
# print(dir(cars))
# print(help(cars))
print(len(cars))
print("BMW" in cars)
cars[2] = "fjsddgjfdg"
# print(cars)
cars.append("pineapple")
cars.remove("fjsddgjfdg")
cars.insert(5, "Toyota")
cars.sort()
cars.reverse()
# cars.clear()
print(cars)
