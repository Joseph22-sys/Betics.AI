from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField,SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length



class Userdata(FlaskForm):
    age = IntegerField("age",validators=[DataRequired(),InputRequired()])
    gender = SelectField("gender" ,choices=[("1", "Male"), ("0", "Female")], validators=[DataRequired(), InputRequired()])
    
    pulse_rate = IntegerField("pulse_rate",validators=[DataRequired(),InputRequired()])
    
    systolic_bp = IntegerField("systolic_bp",validators=[DataRequired(),InputRequired()])
    diastolic_bp = IntegerField("diastolic_bp",validators=[DataRequired(),InputRequired()])
    glucose = FloatField("glucose",validators=[DataRequired(),InputRequired()])
    height = FloatField("height",validators=[DataRequired(),InputRequired()])
    weight = FloatField("weight",validators=[DataRequired(),InputRequired()])
    
    family_diabetes = SelectField("Family Diabetes", choices=[("1", "Yes"), ("0", "No")])
    hypertensive = SelectField("Hypertensive", choices=[("1", "Yes"), ("0", "No")])
    family_hypertension = SelectField("Family Hypertension", choices=[("1", "Yes"), ("0", "No")])
    cardiovascular_disease = SelectField("Cardiovascular Disease", choices=[("1", "Yes"), ("0", "No")])
    stroke = SelectField("Stroke", choices=[("1", "Yes"), ("0", "No")])
    submit = SubmitField("Predict Diabetes")

    
    
    
    
    
    
    
    
    
    
