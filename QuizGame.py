questions = (
    "What is the largest planet in our Solar System?:",
    "What is the capital city of Japan?:",
    "Which element has the chemical symbol O?:",
    "How many continents are commonly recognized on Earth?:",
    "Who wrote the novel Pride and Prejudice?:",
    "Which ocean is the largest on Earth?:",
    "What is the hardest naturally occurring mineral?:",
    "Which planet is known as the Red Planet?:",
    "Which organ pumps blood throughout the human body?:",
    "What is 15 × 6?:")

options = (("A. Saturn", "B. Neptune", "C. Jupiter", "D. Earth"),
                ("A. Hiroshima", "B. Kyoto", "C. Osaka", "D. Tokyo"),
                ("A. Gold", "B. Iron", "C. Osmium", "D. Oxygen"),
                ("A. Eight", "B. Seven", "C. Six", "D. Five"),
                ("A. Emily Brontë", "B. Jane Austen", "C. Charlotte Brontë", "D. Mary Shelley"),
                ("A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. Arctic Ocean"),
                ("A. Diamond", "B. Quartz", "C. Granite", "D. Calcite"),
                ("A. Uranus", "B. Mars", "C. Mercury", "D. Venus"),
                ("A. Heart", "B. Liver", "C. Lungs", "D. Kidneys"),
                ("A. 90", "B. 85", "C. 95", "D. 80"))
answer = ("C", "D", "D", "B", "B", "A", "A", "B", "A", "A")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("---------------------------------------------")
    print(question)
    for option in options[questions_num]:
            print(option)

    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answer[questions_num]:
        score += 1
    questions_num += 1

print("---------------------------------------------")
print("RESULTS")
print("---------------------------------------------")
# print("Answers: ", end="")
# for ans in answer:
#     print(ans, end=" ")
# print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"Your score is: {score}/{len(questions)} ({(score/len(questions))*100:.2f}%)")