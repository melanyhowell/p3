from munch import db


recipe_category = db.Table("recipe_category",
                           db.Column("recipe_id", db.Integer,
                                     db.ForeignKey("recipe.id")),
                           db.Column("category_id", db.Integer,
                                     db.ForeignKey("category.id"))
                           )


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ representing itself in the form of a string
        return self.category_name


class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(55), unique=True, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    recipe_cook_temp = db.Column(db.Integer, nullable=False)
    recipe_prep_time = db.Column(db.Integer, nullable=False)
    recipe_cook_time = db.Column(db.Integer, nullable=False)
    # recipe_ingredients = db.Column(db.String, nullable=False)
    categories = db.relationship("Category", secondary=recipe_category,
                                 backref="recipes")

    def __repr__(self):
        return self.recipe_name
