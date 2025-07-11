from app.model import bp
from flask import render_template,session, redirect, url_for,request
from app.user.data_validator import Userdata
from app.model.utils import get_bmi,get_risk_score,get_bmi_category,run_prediction



@bp.route('/predict',methods=["POST"])
def predict():
    form = Userdata()
    if request.method == "POST":
        if form.validate_on_submit():
            age = int(form.age.data)
            gender = int(form.gender.data)
            
            pulse_rate = int(form.pulse_rate.data)  
            systolic_bp = int(form.systolic_bp.data)
            diastolic_bp = int(form.diastolic_bp.data)   
            glucose = float(form.glucose.data)
            height = float(form.height.data)
            weight = float(form.weight.data)
            
            
            family_diabetes = form.family_diabetes.data
            hypertensive = form.hypertensive.data   
            family_hypertension = form.family_hypertension.data
            cardiovascular_disease = form.cardiovascular_disease.data
            stroke = form.stroke.data
            
            bmi = get_bmi(weight, height)
            risk_score = get_risk_score(glucose, bmi, age)
            bmi_category = get_bmi_category(bmi)
            
           
            user_data = [age,gender,pulse_rate,systolic_bp,diastolic_bp,
                         glucose,height,weight,bmi,family_diabetes,
                         hypertensive,family_hypertension,cardiovascular_disease,
                         stroke,bmi_category,risk_score]

            
            run_prediction(user_data)
            
            return redirect(url_for('user.dashboard'))
    
    return render_template("data_entry.html", title="Data Entry")