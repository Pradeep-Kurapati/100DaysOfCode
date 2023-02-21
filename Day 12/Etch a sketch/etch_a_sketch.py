from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


timmy.width(2)


def move_right():
    timmy.forward(10)


def move_left():
    timmy.backward(10)


def rotate_right():
    timmy.setheading(timmy.heading() + 10)


def rotate_left():
    timmy.setheading(timmy.heading() - 10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()

screen.onkey(move_right, "w")
screen.onkey(move_left,'s')
screen.onkey(rotate_left, 'a')
screen.onkey(rotate_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()
