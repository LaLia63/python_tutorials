# format specifiers = {:flags} format a value based on what
#                                 flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# : (number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# + = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 356456.23224
price2 = -5646.445443
print(f"price1 is ${price1:.3f}")
print(f"price2 is ${price2:.3f}")
print(f"------------------------------")
print(f"price1 is ${price1:.3}")
print(f"price2 is ${price2:.3}")
print(f"------------------------------")
print(f"price1 is ${price1:09}")
print(f"price2 is ${price2:09}")
print(f"------------------------------")
print(f"price1 is ${price1:<10}")
print(f"price2 is ${price2:<10}")
print(f"------------------------------")
print(f"price1 is ${price1:>10}")
print(f"price2 is ${price2:>10}")
print(f"------------------------------")
print(f"price1 is ${price1:^10}")
print(f"price2 is ${price2:^10}")
print(f"------------------------------")
print(f"price1 is ${price1:+}")
print(f"price2 is ${price2:+}")
print(f"------------------------------")
print(f"price1 is ${price1: }")
print(f"price2 is ${price2: }")
print(f"------------------------------")
print(f"price1 is ${price1:,.2f}")
print(f"price2 is ${price2:,.2f}")
print(f"------------------------------")
