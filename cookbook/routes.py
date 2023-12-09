from flask import render_template
from cookbook import app, db
from cookbook.models import User, Recipe 

@app.route("/")
def index():
    return render_template("index.html")