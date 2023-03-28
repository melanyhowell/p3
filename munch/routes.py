from flask import render_template
from munch import app, db
from munch.models import Category, Recipe


@app.route("/")
def home():
    return render_template("add_recipe.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    return render_template("add_recipe.html")
