from flask import render_template
from p3 import app, db


@app.route("/")
def home():
    return render_template("base.html")
