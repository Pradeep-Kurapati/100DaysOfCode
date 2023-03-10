from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def recieve_data():
    username = request.form['username']
    password = request.form['password']
    return f"<h1>Name: {username}, Password: {password}</h1>"