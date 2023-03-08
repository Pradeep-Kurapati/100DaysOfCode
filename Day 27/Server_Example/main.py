from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def Hello_world():
    return render_template("pradeep.html")
