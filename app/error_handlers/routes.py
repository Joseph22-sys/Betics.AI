from app.error_handlers import bp
from flask import render_template

@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="404"), 404


