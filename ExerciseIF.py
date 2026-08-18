response = input("Would you like to continue? (yes/no): ")

if response.lower() == "yes":
    print("You chose to continue.")
elif response.lower() == "no":
    print("You chose not to continue.")
elif response.upper() == "YES":
    print("You chose to continue.")
elif response.upper() == "NO":
    print("You chose not to continue.")
elif response == "Yes":
    print("You chose to continue.")
elif response == "No":
    print("You chose not to continue.")
else:
    print("Invalid response. Please enter 'yes' or 'no'.")