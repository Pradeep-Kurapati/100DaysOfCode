import random
# Rock Paper Scissors ASCII Art

# Rock
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
player2 = random.randint(0,2)

if player1 == 0:
    print(rock)
elif player1 == 1:
    print(paper)
else:
    print(scissors)

print("Computer choose:")

if player2 == 0:
    print(rock)
elif player2 == 1:
    print(paper)
else:
    print(scissors)

if player1 == player2:
    print("It's a draw")
elif player1 == 0:
    if player2==2:
        print("You win!")
    else:
        print("You lose.")
elif player1==1:
    if player2==0:
        print("you win!")
    else:
        print("You lose")
elif player1==2:
    if player2==1:
        print("You win!")
    else:
        print("You lose.")