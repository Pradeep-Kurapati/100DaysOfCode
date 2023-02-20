import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
turtle.colormode(255)
timmy.speed(0)

timmy.width(1.45)
def spirograph(gapsize):
    for x in range(int(360/gapsize)):
        t_color = colormaker()
        timmy.pencolor(t_color)
        timmy.circle(150)
        timmy.setheading(timmy.heading()+gapsize)

def colormaker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

gapsize = 5

spirograph(5)
screen.exitonclick()
