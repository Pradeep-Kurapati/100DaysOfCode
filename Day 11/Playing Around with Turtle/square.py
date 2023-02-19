from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("arrow")
timmy.color("ForestGreen")
for _ in range(3):
    timmy.forward(100)
    timmy.left(90)
timmy.forward(100)

screen = Screen()
screen.exitonclick()
