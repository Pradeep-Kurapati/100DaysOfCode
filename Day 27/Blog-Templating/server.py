from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    blog_url = "https://api.npoint.io/7ae592855be9b6823cff"
    response = requests.get(url=blog_url)
    data = response.json()
    return render_template("index.html", data=data)


