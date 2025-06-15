from app.main import bp
from flask import render_template

@bp.route('/')
def home():
    return render_template("home.html")