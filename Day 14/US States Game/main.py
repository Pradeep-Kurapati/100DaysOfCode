from turtle import Turtle
from writer import Writer
import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

state_list = pandas.read_csv('50_states.csv')
states = []

for x in state_list['state']:
    states.append(x)

guess = 0
correct_guess = []
while guess != 51:
    answer_state = screen.textinput(title=f'{guess} / 50', prompt="What's another state:").title()

    if answer_state in states and answer_state not in correct_guess:

        guess += 1
        correct_guess.append(answer_state)
        row = state_list[state_list.state == answer_state]
        new_x = int(row['x'])
        new_y = int(row['y'])
        writer = Writer(new_x, new_y, answer_state)


screen.exitonclick()
