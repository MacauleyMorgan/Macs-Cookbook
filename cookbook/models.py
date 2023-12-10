from cookbook import db

class User(db.Model):
    # Schema for creating user in db
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    recipes = db.relationship("recipe", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        return "#{0} - First Name: {1} Last name:{2} Email: {3} Password: {4} Is admin: {5}".format(
            self.id, self.first_name, self.last_name, self.email, self.password, self.is_admin
        )


class Recipe(db.Model):
    # Schema for creating user in db
    recipe_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))
    recipe_name = db.Column(db.Text, nullable=False)
    recipe_time = db.Column(db.Integer, nullable=False)
    recipe_ingredients = db.Column(db.Text, nullable=False)
    recipe_steps = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "Recipe Name {0} Recipe Time {1} Ingredients {2} Steps {3}".format(
            self.recipe_name, self.recipe_time, self.recipe_ingredients, self.recipe_steps
        )