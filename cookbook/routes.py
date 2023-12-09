from flask import render_template, request
from cookbook import app, db
from cookbook.models import User, Recipe 

@app.route("/", methods =['GET', 'POST'])
def landing():
    if request.method == 'POST':
        email = request.form.get("sign-in-email-address")
        password = request.form.get("password")
        user = [email, password]
        print(user)
    return render_template("landing.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/register", methods =['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        password = request.form.get("password")
        user = [first_name, last_name, email, password]
        print(user)
    return render_template("register.html")


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/add_a_recipe", methods =['GET', 'POST'])
def add_a_recipe():
    if request.method == 'POST':
        recipe_name = request.form.get("rname")
        recipe_time = request.form.get("rtime")
        recipe_ingredients = request.form.get("ringredients")
        recipe_steps = request.form.get("step")
        recipe = [recipe_name, recipe_time, recipe_ingredients, recipe_steps]
        print(recipe)
    return render_template("add_a_recipe.html")