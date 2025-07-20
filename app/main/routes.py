from app.main import bp
from flask import render_template,session



@bp.route('/')
def home():
    session.clear()
    return render_template("home.html")