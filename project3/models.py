from project3 import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_Key=True)
    category_name = db.Column(db.String(30), unique=True, nullable=False)


    def __repr__(self):
        # __repr__ representing itself in the form of a string
        return self.category_name



class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(75), unique=True, nullanle=False)
    recipe_description = db.Column(db.Text, nullable=False)
    
    
