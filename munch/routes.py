from flask import render_template
from munch import app, db
from munch.models import Category, Recipe


@app.route("/")
def home():
    return render_template("base.html")
