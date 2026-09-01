menu = {
    "popcorn": 4.00,
    "pizza": 7.00,
    "fries": 3.00,
    "chips": 2.00,
    "soda": 1.00,
    "water": 1.00,
}
cart = []
total = 0

print("----------MENU----------")
for item, price in menu.items():
    print(f"{item.title()}: ${price:.2f}")
print("----------MENU----------")

while True:
    choice = input("Select an items (q to quit): ").lower()
    if choice == "q":
        break
    elif choice in menu:
        cart.append(choice)
        total += menu[choice]
        print(f"{choice.title()} added to cart. Total: ${total:.2f}")
    else:
        print("Item not found in menu. Please try again.")

print(f"Your total is: ${total:.2f}")