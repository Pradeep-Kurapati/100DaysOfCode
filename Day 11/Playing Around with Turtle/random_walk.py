import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
timmy = Turtle()
screen = Screen()


def colormaker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color


move = [timmy.forward, timmy.backward]
direction = [timmy.right, timmy.left]
angle = [90, 180, 270, 360]
timmy.width(20)
timmy.speed(0)

for _ in range(600):
    turtle_color = colormaker()
    timmy.color(turtle_color)
    selected_move = random.choice(move)
    selected_direction = random.choice(direction)
    selected_angle = random.choice(angle)
    selected_move(60)
    selected_direction(selected_angle)

turtle.done()


screen.exitonclick()
