# Exercise 1 Shopping cart

item = input("Enter the item you want to buy: ")
price = float(input("What is the price?: "))
quantity = int(input("How many do you want to buy?: "))
total = price * quantity

print(f"You are buying {quantity} {item}(s) at ${price:.2f} each for a total of ${total:.2f}.")
