import random
from turtle import Turtle, Screen
import turtle

colors = ['violet', 'blue', 'green', 'orange', 'red', 'orange', 'gold']
y_positions = [-100, -50, 0, 50, 100]

screen = Screen()
screen.setup(width=500, height=400)
user_bet = turtle.textinput('Place your bet', 'What is your bet:')
all_turtles = []
for index in range(5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-250, y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                if user_bet == turtle.pencolor():
                    print(f"You've won! The winner is {turtle.pencolor()}.")
                else:
                    print(f"You've lost! The winner is {turtle.pencolor()}.")
            move = random.randint(1, 10)
            turtle.forward(move)


screen.exitonclick()
