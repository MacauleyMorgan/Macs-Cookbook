from cookbook import db

class User(db.model):
    # Schema for creating user in db
    id = db.Column(db.integer, primary_key=True)
    first_name = db.column(string(25), unique=False, nullable=False)
    recipes = db.relationship("recipe", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        return "#{0} - First Name: {1} Last name:{2}".format(
            self.id, self.first_name, self.is_urgent
        )


class Recipe(db.model):
    # Schema for creating user in db
    id = db.Column(db.integer, db.foreign_key("User.id"), ondelete="CASCADE")
    recipe_name = db.Column(db.text, nullable=False)
    recipe_time = db.Column(db.integer(10), nullable=False)
    recipe_ingredients = db.Column(db.text, nullable=False)

    def __repr__(self):
    return self.recipe_name