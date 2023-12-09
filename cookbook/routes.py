from flask import render_template, render_template
from cookbook import app, db
from cookbook.models import User, Recipe 

@app.route("/")
def landing():
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


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/index")
def index():
    return render_template("index.html")