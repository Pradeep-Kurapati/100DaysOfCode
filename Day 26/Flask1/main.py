from flask import Flask

app = Flask(__name__)


def bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def italicise(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/")
@bold
@italicise
@underline
def hello():
    return "Hi"