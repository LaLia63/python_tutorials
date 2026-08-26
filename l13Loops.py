# for loops = execute a block of code a fixed number of times.
#                   You can iterate over a range, string, sequence, etc.
# reversed used to display from 10 to 1

# for x in range(1, 11, 2):
#     print(x)

# for y in reversed(range(1, 11)):
#     print(y)

# print("Happy New Year!!!")

# credict_card_number = "1234-5678-9012-3456"
# for x in credict_card_number:
#     print(x)

for x in range(1, 21):
    if x == 13:
        continue # don't print num 13
    #  break = stop the iteration and give the result for that display 1 to 12
    else:
        print(x)
