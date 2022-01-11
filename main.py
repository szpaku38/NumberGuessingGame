# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)
print(f"The answer: {answer}")
chances = 0


def choose_difficulty(level):
    if level == "easy":
        print("You have 10 attempts remaining to guess the number.")
        return 10
    elif level == "hard":
        print("You have 5 attempts remaining to guess the number.")
        return 5
    else:
        print("Wrong input. Relaunch the game.")
        exit()


def play_game(guess):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        exit()
    elif guess > answer and chances > 0:
        print("Too high.")
    elif guess < answer and chances > 0:
        print("Too low.")


chances = choose_difficulty(
    input("Choose a difficulty. Type 'easy' or 'hard': "))

while chances > 0:
    play_game(int(input("Make a guess: ")))
    chances -= 1
    print(f"You have {chances} attempts remaining to guess the number.")

print("You lost all your chances. You lose.")
