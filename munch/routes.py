from flask import render_template, request, redirect, url_for
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
    if request.method == "POST":
        recipe = Recipe(recipe_name=request.form.get("recipe_name"))
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("recipes"))
    return render_template("add_recipe.html")
