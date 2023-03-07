from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<b><h1>Guess a number between 0 and 9<h1></b>" \
           "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='countdown'/>"


number = random.randint(0, 9)

@app.route('/<int:num>')
def show(num):
    if num == number:
        return "<h1>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif num < number:
        return "<h1>Too low</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return "<h1>Too High</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
