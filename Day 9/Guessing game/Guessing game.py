import random
from art import logo1

print(logo1)

def start():
    print("Welcome to guessing game!")
    number = random.randint(1,100)
    done = False
    while done == False:
        choice = input("Choose 'easy' or 'hard': ")
        if choice == 'easy' or choice =='e':
            attempt = 10
            done = True
        elif choice == 'hard' or choice =='h':
            attempt = 5
            done = True
        else:
            print("Try again.")
    game = 's'
    while attempt != 0 and game != 'over':
        guess = int(input(f"You have {attempt} attempt(s) to guess the number.\nMake a guess: "))
        if guess > number:
            print("Too high.")
            attempt -= 1
            if attempt != 0:
                print("Guess again.")
        elif guess < number:
            print("Too low.")
            attempt -= 1

            if attempt != 0:
                print("Guess again.")
        else:
            print(f"You got it! The answer was {number}.")
            game = 'over'

    if attempt == 0:
        print(f"You've run out of guesses. You lose.\nThe answer was {number}")

    done = False

    while done == False:
        game = input("Do you want to play again? 'Yes' or 'no'\n").lower()
        if game == 'yes' or game == 'y':
            start()
            done = True
        elif game == 'no' or game == 'n':
            done = True
        else:
            print("Try again. Invalid input")

start()


