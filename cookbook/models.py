from flask import render_template
from cookbook import app, db
from cookbook.models import User, Recipe 

@app.route("/")
def home():
    return render_template("base.html")