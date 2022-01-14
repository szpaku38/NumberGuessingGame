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
