foods = []
prices = []
total = 0

while True:
    food = input("Enter your items: ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter your price for {food}: $"))
        foods.append(food)
        prices.append(price)

print(f"----------YOUR CART----------")
for food in foods:
    print(food, end = " ")
print()

for price in prices:
    total += price
print(f"Your total is: ${total}")