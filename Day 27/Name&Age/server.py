from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/guess/<name>")
def guess(name):
    age_url = f"https://api.agify.io?name={name}"
    response = requests.get(url=age_url)
    age = response.json()['age']
    gender_url = f'https://api.genderize.io/?name={name}'
    response = requests.get(url=gender_url)
    gender = response.json()["gender"]
    return render_template("index.html", name=name, age=age, gender=gender)


@app.route("/")
def home():
    return "<h1>Hello 👋🏽</h1>"

