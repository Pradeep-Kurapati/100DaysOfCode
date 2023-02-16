import random
from word_list import wordlist

stages = [
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]
print(
    '''
    
 __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. 
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| 
       
                                                                                
    '''
)


print("Welcome to Hangman game.")

def hangman():
    print(
        '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
    )
    guess_list=[]
    word = random.choice(wordlist)
    count = 0
    end = False
    display = []
    for x in range(len(word)):
        display += '_'
    print(display)

    while not end and count!=6:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You already guessed {guess}!\n")

        for position in range(len(word)):
            letter = word[position]
            if letter == guess:
                display[position] = guess
        print(display)

        if guess not in word:
            print(f"You guessed {guess}, that is not in the word. You lose a life!\n\n")
            if count == 6:
                end = True
                print("You lose.")
            else:
                print(stages[count])
                count+=1

        if '_' not in display:
            end = True
            print("You win!")

    if count ==6:
        print("You lose.")

hangman()

choice = input("Do you want to play again? Yes(y) No(n)").lower()
if choice == 'y':
    hangman()
else:
    print("Thank you for playing. Come back next time!")
    exit()


