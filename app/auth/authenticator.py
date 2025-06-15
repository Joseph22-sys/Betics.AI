from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired,InputRequired, Length,Email,EqualTo


class Signup(FlaskForm):
    username = StringField("username",validators=[DataRequired(),InputRequired(),Length(min=3,max=30)])
    email = EmailField("email",validators=[DataRequired(),Email(message='Invalid email format')])
    phone = StringField("phone number",validators=[InputRequired(), Length(min=10,max=15)])
    password = PasswordField("password",validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("password",validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Signup")
    
class Login(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(),InputRequired(),Email()])
    password = PasswordField("password",validators=[DataRequired(), Length(min=2)]) 
    submit = SubmitField("Login")
    
    
