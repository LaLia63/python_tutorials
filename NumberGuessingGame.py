import random
lowest_num = 1
highest_num = 100
number = random.randint(lowest_num, highest_num)
guess_time = 0
guess = 0

while guess != number:
    guess = input(f"Guess a number between {lowest_num} and {highest_num}: ")
    if guess.isdigit():
        pass
    else:
        print("Please enter a valid number.")
        continue
    if int(guess) < number:
        print("Too low! Try again.")
        guess_time += 1
    elif int(guess) > number:
        print("Too high! Try again.")
        guess_time += 1
    else:
        print(f"Congratulations! You've guessed the correct number: {number} in {guess_time} attempts.")