fruits          = ["apple", "orange", "banana", "grape", "mango"]
vegetables = ["carrot", "broccoli", "spinach", "kale", "pepper"]
cars            = ["toyota", "honda", "ford", "chevrolet", "nissan"]

items = [fruits, vegetables, cars]

for category in items:
    print(f"Category: {category[0]}")
    for item in category:
        print(f"- {item}")
    print()

num_pad = ((1, 2, 3),
                    (4, 5, 6),
                    (7, 8, 9),
                    ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()
                        