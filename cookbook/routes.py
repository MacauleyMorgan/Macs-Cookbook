from flask import render_template, request, redirect, flash, url_for, session
from cookbook import app, db
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
            user_already_exists = User.query.filter(
            User.email == request.form.get("email").lower()).all()
            # If none, flash message (does not exist)#
            if user_already_exists:
                flash("Email does not exist")
                return redirect(url_for("landing.html"))
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
                return redirect(url_for("landing"))
                flash("Email already in use")
            # Step 3 If not, create a new user
            new_user = User(
                first_name = request.form.get("first-name").lower(),
                last_name = request.form.get("last-name").lower(),
                email = request.form.get("email").lower(),
                password = request.form.get("password").lower(),
                is_admin = False,
                recipes = []
            )
            print(new_user, "Added")
            db.session.add(new_user)
            db.session.commit()
            # Step 4 Add user to database
            # Step 5 if admin is true, redirect to admin page, else send to index page
            # Step 6 Flash message to feedback success
            redirect(url_for("register"))
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