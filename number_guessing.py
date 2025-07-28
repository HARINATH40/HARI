import random
import os

def play_game(player_name):
    print(f"\n🎮 Welcome, {player_name}, to the Number Guessing Game!")
    print("Choose difficulty: easy / medium / hard")
    difficulty = input("Your choice: ").strip().lower()

    if difficulty == "easy":
        max_number = 50
        max_attempts = 10
    elif difficulty == "medium":
        max_number = 100
        max_attempts = 7
    elif difficulty == "hard":
        max_number = 200
        max_attempts = 5
    else:
        print("Invalid choice. Defaulting to medium.")
        max_number = 100
        max_attempts = 7

    number = random.randint(1, max_number)
    attempts = 0

    print(f"I'm thinking of a number between 1 and {max_number}. You have {max_attempts} attempts!")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} tries.")
                return 1
        except ValueError:
            print("⚠️ Please enter a valid number.")

    print(f"❌ Out of attempts! The number was {number}.")
    return 0

# Ask for player name
player_name = input("Enter your name: ").strip().title()

# Load high score and high scorer from file
high_score = 0
high_scorer = "None"

if os.path.exists("highscore.txt"):
    with open("highscore.txt", "r") as file:
        try:
            lines = file.readlines()
            if len(lines) == 2:
                high_score = int(lines[0])
                high_scorer = lines[1].strip()
        except:
            pass

# Main game loop
score = 0

while True:
    score += play_game(player_name)
    print(f"🏆 {player_name}'s current score: {score}")
    print(f"🥇 High Score: {high_score} by {high_scorer}")

    if score > high_score:
        with open("highscore.txt", "w") as file:
            file.write(f"{score}\n{player_name}")
        high_score = score
        high_scorer = player_name
        print("🎉 New High Score!")

    again = input("Do you want to play again? (yes/no): ")
    if again.strip().lower() in ("no", "n"):
        print(f"Thanks for playing, {player_name}! Final Score: {score}")
        break
