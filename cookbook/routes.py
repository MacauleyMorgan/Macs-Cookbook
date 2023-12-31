from flask import render_template, request, redirect, flash, url_for, session
from cookbook import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from cookbook.models import User, Recipe 

@app.route("/", methods =['GET', 'POST'])
def landing():
    if request.method == 'POST':
        """
        This function will map the logic of logging in by checking existing users
        After finding the matching entry, a password check will be completed
        """
        # Check if email exists
        if request.method == "POST":
            # If none, flash message (does not exist)#
            # If it does, check the password matches
            # If not, flash message (incorrect password)
            # If admin, direct to admin page
            # If user, direct to index.html
    return render_template("landing.html")
    

@app.route("/register", methods =['GET', 'POST'])
def register():
    if request.method == 'POST':
        """
        This function will take the username and check if it exists on the database
        If not, it will create a user
        """
        # Step 1 Check if email exists
        if request.method == "POST":
            user_already_exists = User.query.filter(
            User.email == request.form.get("email").lower()).all()
            # Step 2 If user exists flask a feedback message
            if user_already_exists:
                print("Email already in use")
                flash("Email already in use")
                return redirect(url_for("landing"))
            # Step 3 If not, create a new user
            new_user = User(
                first_name = request.form.get("first-name").lower(),
                last_name = request.form.get("last-name").lower(),
                email = request.form.get("email").lower(),
                password = generate_password_hash(request.form.get("password")),
                is_admin = False,
                recipes = []
            )
            print(new_user, "Added")
            # Step 4 Add user to database
            db.session.add(new_user)
            db.session.commit()
            # Step 6 Flash message to feedback success
            flash("Success! Welcome to the site")
            print("Success! Welcome to the site")
            redirect(url_for("landing"))
    return render_template("register.html")



@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/index")
def index():
    return render_template("index.html")
    

@app.route("/admin")
def admin():
    return render_template("admin.html")



@app.route("/add_a_recipe", methods =['GET', 'POST'])
def add_a_recipe():
    if request.method == 'POST':
        # Gets recipe submission
        recipe_name = request.form.get("rname")
        recipe_time = request.form.get("rtime")
        recipe_ingredients = request.form.get("ringredients")
        # Need to come back to this and make a for loop for steps
        recipe_steps = [request.form.get("step")]
        recipe = [recipe_name, recipe_time, recipe_ingredients, recipe_steps]
        print(recipe)
    return render_template("add_a_recipe.html")