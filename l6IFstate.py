# if = Do some code only IF some condition is True
#       Else do something else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
elif age <= 0:
        print("Please enter a valid age.")
else:
    print("You are a minor.")
