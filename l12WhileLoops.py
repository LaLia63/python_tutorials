# While Loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")
age = int(input("Enter your age: "))

while name == "":
    print("You didn't enter your name")
    name = input("Enter your name: ")
while age <= 0:
    print("Invalid age")
    age = int(input("Enter your age: "))
print(f"Hello {name}! You are {age} years old")
