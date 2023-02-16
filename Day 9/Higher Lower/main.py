from game_data import data
import random
from art import logo, vs
# from replit import clear
# remove the comments if you're going to use this code on Replit
# for better user experience.

def decider(op1, op2):
    if op1['follower_count'] > op2['follower_count']:
        return op1
    else:
        return op2


def start():
    score = 0
    c1 = random.choice(data)
    c2 = random.choice(data)
    while c1 == c2:
        c2 = random.choice(data)
    print(logo)
    answer = decider(c1, c2)
    if answer == c1:
        correct = 'a'
    else:
        correct = 'b'
    print(f"Compare A: {c1['name']}, a {c1['description']}, from {c1['country']}")
    print(vs)
    print(f"Compare B: {c2['name']}, a {c2['description']}, from {c2['country']}")
    choice = input("Who has more followers? A or B: ").lower()
    if choice == correct:
        score += 1
        game_continue(answer, score)
    else:
        print("Sorry, That's wrong.")


def game_continue(answer, score):
    b = random.choice(data)
    while answer == b:
        b = random.choice(data)
    # clear()
    print(logo)
    print(f"You're right! Score: {score}")
    print(f"Compare A: {answer['name']}, a {answer['description']}, from {answer['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']} ")
    correct = decider(answer, b)
    if correct == answer:
        option = 'a'
    else:
        option = 'b'
    choice = input("Who has more followers? A or B: ").lower()
    if choice == option:
        score += 1
        answer = correct
        game_continue(answer, score)
    else:
        print(f"Sorry, that's wrong. Your score: {score}")


start()
