from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGNMENT = 'center'
GAME_POSITION = (-233, 255)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(GAME_POSITION)
        self.display()
        self.hideturtle()

    def display(self):
        self.clear()
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.goto(GAME_POSITION)
        self.display()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('Game Over.', align=ALIGNMENT, font=('Courier', 24, 'normal'))
