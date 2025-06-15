from flask import Blueprint 

bp = Blueprint("error_handlers",__name__)

from app.error_handlers import routes