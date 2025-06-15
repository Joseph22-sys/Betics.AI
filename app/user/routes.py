from app.user import bp
from flask import render_template

@bp.route('/dashboard')
def dashboard():
    return "Wow me made we login"

