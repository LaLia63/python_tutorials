import random

options = ("rock", "paper", "scissors")

player = input("Enter your choice (rock, paper, scissors): ").lower()

while player not in options:
    print("Invalid choice. Please try again.")
    player = input("Enter your choice (rock, paper, scissors): ").lower()

computer = random.choice(options)

print(f"You selected: {player}")
print(f"Computer selected: {computer}")

if player == computer:
    print(f"Both players selected {player}. It's a tie!")

elif player == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")

elif player == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")

elif player == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")