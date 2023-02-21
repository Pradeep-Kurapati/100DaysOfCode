from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 275)
        self.color('white')
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'Score : {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over.',align=ALIGNMENT, font=FONT)


    def increase(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
