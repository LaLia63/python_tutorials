# Variable = A Container for a value (String, intege, float, boolean)
#                 A Variable behave as if it was the value it contains

# Strings
first_name = "Lia"
food = "Hotpot"
email = "lia123@fake.com"

print(f"Hello. I am {first_name}!")
print(f"I like {food}.")
print(f"My Email is {email}.")

# Integers
age = 25
quantity = 3
no_of_student = 30

print(f"I am {age} years old.")
print(f"I am buying {quantity} items.")
print(f"My class has {no_of_student} students.")

# Float
price = 10.99
gpa = 3.5
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is{gpa}")
print(f"The distance is {distance}km")


# Boolean
is_student = False
for_sale = True
is_online = True

print(f"Are you a studnet?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("you are NOT a student")

if for_sale:
    print("This care is for Sale")
else:
    print("This car is NOT for Sale")
    
if is_online:
    print("That person is online currently")
else:
    print("This person is offline currently")
