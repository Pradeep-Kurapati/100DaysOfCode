from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 10, 'normal')


class Writer(Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.color('black')
        self.penup()
        self.goto(x, y)
        # self.write(state, align=ALIGNMENT, font=FONT)
        self.write(state)
        self.hideturtle()
