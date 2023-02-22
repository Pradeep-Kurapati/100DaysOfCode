from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title('My Pong Game')
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-389, 0))
r_scoreboard = Scoreboard((100, 200))
l_scoreboard = Scoreboard((-100, 200))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


is_game_on = True
while is_game_on:
    time.sleep(ball.pace)
    screen.update()
    ball.move()
    # Detecting collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detecting Collision with Paddles
    if ball.xcor() > 359 and ball.distance(r_paddle) < 55 or ball.xcor() < -360 and ball.distance(l_paddle) < 50:
        ball.bounce_paddle()

    # Detecting if paddle misses the screen.
    if ball.xcor() > 400:
        l_scoreboard.increase()
        ball.restart()

    if ball.xcor() < -400:
        r_scoreboard.increase()
        ball.restart()

screen.exitonclick()
