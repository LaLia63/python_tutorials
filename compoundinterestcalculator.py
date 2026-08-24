principle = 0
rate = 0
time = 0

# while principle < 0:
#         principle = int(input("Enter your Principle: "))
#         if principle < 0:
#             print("Principle can't be less than zero")

# while rate < 0:
#         rate = int(input("Enter your Rate: "))
#         if rate < 0:
#             print("Rate can't be less than zero")

# while time < 0:
#         time = int(input("Enter your Time: "))
#         if time < 0:
#             print("Time can't be less than zero")
# total = principle * pow((1 + rate /100), time)

while True:
        principle = int(input("Enter your Principle: "))
        if principle < 0:
            print("Principle can't be less than zero")
        else:
            break

while True:
        rate = int(input("Enter your Rate: "))
        if rate < 0:
            print("Rate can't be less than zero")
        else:
            break

while True:
        time = int(input("Enter your Time: "))
        if time < 0:
            print("Time can't be less than zero")
        else:
            break
total = principle * pow((1 + rate /100), time)

print(f"Balance after {time} year/s: ${total:.2f}")
