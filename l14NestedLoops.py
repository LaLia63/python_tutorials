# nested loopI= A loop within another loop (outer, inner)
#                        outer loop:
#                        inner loop:

rows = int(input("Enter you # of rows: "))
columns = int(input("Enter you # of columns: "))
symbols = input("Enter you symbols: ")

for x in range(rows):
    for y in range (columns):
        print(symbols, end = " ")
    print()
    