from flask import render_template, request, redirect, url_for
from munch import app, db
from munch.models import Recipe, Category


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/recipes")
def recipes():
    recipes = list(Recipe.query.order_by(Recipe.recipe_name).all())
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            recipe_description=request.form.get("recipe_description"),
            recipe_cook_temp=request.form.get("recipe_cook_temp"),
            recipe_prep_time=request.form.get("recipe_prep_time"),
            recipe_cook_time=request.form.get("recipe_cook_time"),
            recipe_ingredients1=request.form.get("recipe_ingredients1")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("recipes"))
    return render_template("add_recipe.html")


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name")
        recipe.recipe_description = request.form.get("recipe_description")
        recipe.recipe_cook_temp = request.form.get("recipe_cook_temp")
        recipe.recipe_prep_time = request.form.get("recipe_prep_time")
        recipe.recipe_cook_time = request.form.get("recipe_cook_time")
        recipe.recipe_ingredients1 = request.form.get("recipe_ingredients1")
        db.session.commit()
        return redirect(url_for("recipes"))
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("recipes"))
