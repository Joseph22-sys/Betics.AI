from flask import Flask
from config import Config
from app.extensions import db
from app.db_models.auth import User


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # App blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    
    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')
    
    from app.model import bp as model_bp
    app.register_blueprint(model_bp, url_prefix='/model')
    
    from app.error_handlers import bp as error_handlers_bp
    app.register_blueprint(error_handlers_bp)

 

    # Create tables automatically on first run
    with app.app_context():
        db.create_all()
    
    
    return app
