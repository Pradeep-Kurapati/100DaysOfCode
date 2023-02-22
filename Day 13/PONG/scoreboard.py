from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 75, 'normal')


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.value = 0
        self.color('white')
        self.write(f'{self.value}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase(self):
        self.clear()
        self.value += 1
        self.write(f'{self.value}', align=ALIGNMENT, font=FONT)
