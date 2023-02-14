import os
print(
    '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
    '''
)
finish = False
auction = {}
while finish == False:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    auction[name] = bid
    stop = input("Are there other bidders?\n Yes(y) or No(n)\n").lower()
    if stop=='n':
        finish = True
    os.system('cls')



max = -1
for x in auction:
    if auction[x] > max:
        max = auction[x]
        winner = x

print(
    '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
    '''
)
print(f"Winner is {winner} with a bid of ${max}")P

