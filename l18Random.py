import random

low = 1
high  = 100
choices = ["rock", "paper", "scissors"]
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# number = random.randint(low, high)
# choice = random.choice(choices)
card = random.choice(cards)
random.shuffle(cards)



print(cards)