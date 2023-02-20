import random
import turtle
from turtle import Turtle, Screen

# import colorgram
#
# colors = colorgram.extract('image.jpg', 10)
# color_list = []
# for x in colors:
#     red = x.rgb[0]
#     green = x.rgb[1]
#     blue = x.rgb[2]
#     color_tuple = (red, green, blue)
#     color_list.append(color_tuple)
# print(color_list)
color_list = [
    (224, 150, 101), (25, 103, 181), (157, 79, 44),
    (182, 14, 37), (161, 54, 95), (242, 228, 94), (142, 120, 163),
    (85, 120, 163), (154, 53, 73)
]

turtle.colormode(255)
timmy = Turtle()
timmy.color('white')
timmy.setposition(0, -200)
screen = Screen()
timmy.width(20)
stop = False
timmy.speed(0)

count = 0


def function1():
    global count
    while count != 10:
        for _ in range(10):
            timmy.pendown()
            timmy.dot(25, random.choice(color_list))
            timmy.penup()
            timmy.forward(50)
        count += 1
        move()


def move():
    a = timmy.pos()[0]
    b = timmy.pos()[1]
    timmy.setposition(0, b + 50)
    function1()


function1()

screen.exitonclick()
