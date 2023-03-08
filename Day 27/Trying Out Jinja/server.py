from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.date.today().year
    return render_template("index.html", current_year=year)
