
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def adder(player):
    card = random.choice(cards)
    if card == 11 and sum(player) + card > 21:
        card = 1
    player.append(card)
    return player


def start():
    print(logo)
    choice = input("Do you want to play Blackjack? Yes(y) or No(n)\n")
    if choice == 'y':
        player = []
        computer = []
        for _ in range(2):
            player = adder(player)
            computer = adder(computer)
        print(f"Your cards are {player}, current score: {sum(player)}\nComputer's first card: {computer[0]}")
        game_continue(player, computer)
    else:
        exit()


def game_continue(player, computer):
    choice = input("Type 'y' to get new card, 'n ' to pass: ")
    if choice == 'y':
        player = adder(player)
        if sum(player) == 21:
            print("You win!")
            print(
                f"Your final hand is {player}. Your total score: {sum(player)}.\nComputer's final hand is {computer}. Computer total score: {sum(computer)}")
            start()
        elif sum(player) > 21:
            print("You lose!")
            print(
                f"Your final hand is {player}. Your total score: {sum(player)}.\nComputer's final hand is {computer}. Computer total score: {sum(computer)}")
            start()
        else:
            print(f"Your hand is {player}. Current score: {sum(player)}\nComputer's hand: {computer[0]}.")
            game_continue(player, computer)
    else:
        if sum(computer) == sum(player):
            print("It's a Draw.")
            print(
                f"Your final hand is {player}. Your total score: {sum(player)}.\nComputer's final hand is {computer}. Computer total score: {sum(computer)}")
            start()
        elif sum(player) > sum(computer):
            print("You win!")
            print(
                f"Your final hand is {player}. Your total score: {sum(player)}.\nComputer's final hand is {computer}. Computer total score: {sum(computer)}")
            start()
        elif sum(computer) > sum(player) and sum(computer) < 21:
            print("You lose!")
            print(
                f"Your final hand is {player}. Your total score: {sum(player)}.\nComputer's final hand is {computer}. Computer total score: {sum(computer)}")
            start()
        elif sum(computer) > 21:
            print("You win!")
            print(
                f"Your final hand is {player}. Your total score: {sum(player)}.\nComputer's final hand is {computer}. Computer total score: {sum(computer)}")
            start()


start()







