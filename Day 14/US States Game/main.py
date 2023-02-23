from writer import Writer
import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

state_list = pandas.read_csv('50_states.csv')

# Alternative Method
# states = []
#
# for x in state_list['state']:
#     states.append(x)

states = state_list['state'].to_list()

guess = 0
correct_guess = []
while len(correct_guess) <= 50:
    answer_state = screen.textinput(title=f'{guess} / 50', prompt="What's another state:").title()
    if answer_state == 'Exit':
        break

    elif answer_state in states and answer_state not in correct_guess:

        guess += 1
        correct_guess.append(answer_state)
        row = state_list[state_list.state == answer_state]

        # new_x = int(row['x'])
        # new_y = int(row['y'])
        # writer = Writer(new_x, new_y, answer_state)

        writer = Writer(int(row.x), int(row.y), answer_state)

missed = []
# states_to_learn.csv
for x in states:
    if x not in correct_guess:
        missed.append(x)

missed = pandas.DataFrame(missed, columns=['Missed State'])
missed.to_csv('missed.csv', index=False)
print(pandas.read_csv('missed.csv'))

