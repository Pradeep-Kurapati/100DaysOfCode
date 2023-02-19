from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

colors = ["DeepSkyBlue2", "green4", "HotPink4", "DodgerBlue4", "MidNightBlue"]
used = []

def draw(sides):
    t_color = "black"
    angle = 360/sides
    t_color = random.choice(colors)
    used.append(t_color)
    for _ in range(sides):
        timmy.color(t_color)
        timmy.forward(100)
        timmy.right(angle)


def start():
    for x in range(3, 11):
        side = x
        draw(side)


start()

screen.exitonclick()
