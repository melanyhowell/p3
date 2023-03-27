from flask import render_template
from project3 import app, db
from project3.models import Category, Recipe


@app.route("/")
def home():
    return render_template("base.html")
