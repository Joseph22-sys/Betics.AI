from app.extensions import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    #class variables
    id = db.Column(db.Integer,primary_key=True)
    phone_number = db.Column(db.Integer,nullable=False)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), nullable=False)
    
    def set_password(self,password):
        self.password = generate_password_hash(password)
        
    def check_password(self,password):
        return check_password_hash(self.password,password)
