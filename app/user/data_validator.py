from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField,SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length



class Userdata(FlaskForm):
    age = IntegerField("age",validators=[DataRequired(),InputRequired(),Length(min=1,max=110)])
    gender = SelectField("gender" ,choices=[("1", "Yes"), ("0", "No")], validators=[DataRequired(), InputRequired()])
    
    pulse_rate = IntegerField("pulse_rate",validators=[DataRequired(),InputRequired(),Length(min=40,max=180)])
    systolic_bp = IntegerField("systolic_bp",validators=[DataRequired(),InputRequired(),Length(min=80,max=200)])
    diastolic_bp = IntegerField("diastolic_bp",validators=[DataRequired(),InputRequired(),Length(min=50,max=130)])
    glucose = FloatField("glucose",validators=[DataRequired(),InputRequired(),Length(min=70,max=300)])
    height = FloatField("height",validators=[DataRequired(),InputRequired(),Length(min=1,max=300)])
    weight = FloatField("weight",validators=[DataRequired(),InputRequired(),Length(min=1,max=500)])
    
    family_diabetes = SelectField("Family Diabetes", choices=[("1", "Yes"), ("0", "No")])
    hypertensive = SelectField("Hypertensive", choices=[("1", "Yes"), ("0", "No")])
    family_hypertension = SelectField("Family Hypertension", choices=[("1", "Yes"), ("0", "No")])
    cardiovascular_disease = SelectField("Cardiovascular Disease", choices=[("1", "Yes"), ("0", "No")])
    stroke = SelectField("Stroke", choices=[("1", "Yes"), ("0", "No")])
    submit = SubmitField("Predict Diabetes")

    
    
    
    
    
    
    
    
    
    
    
from wtforms import 