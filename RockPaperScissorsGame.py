import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("=" * 40)
print("     ROCK PAPER SCISSORS GAME")
print("=" * 40)

while True:

    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user = input("Enter your choice (rock/paper/scissors): ").lower()

    if user not in choices:
        print("Invalid Choice! Try Again.")
        continue

    computer = random.choice(choices)

    print("\nYour Choice     :", user)
    print("Computer Choice :", computer)

    if user == computer:
        print("Result : It's a Draw!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):

        print("Result : You Win!")
        user_score += 1

    else:
        print("Result : Computer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print("You      :", user_score)
    print("Computer :", computer_score)

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        break

print("\n" + "=" * 40)
print("           FINAL SCORE")
print("=" * 40)
print("You      :", user_score)
print("Computer :", computer_score)

if user_score > computer_score:
    print("🏆 Congratulations! You are the Winner.")
elif computer_score > user_score:
    print("🤖 Computer Wins the Game.")
else:
    print("🤝 The Game is Draw.")

print("\nThank You for Playing!")