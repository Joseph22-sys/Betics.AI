from app.user import bp
from flask import render_template,session, redirect, url_for,request
from app.user.data_validator import Userdata


@bp.route('/dataentry',methods=["GET","POST"])
def dataentry():
    form = Userdata()
    # if 'username' not in session:
    #     return redirect(url_for('auth.signup'))
    if request.method == "POST":
        if form.validate_on_submit():
            age = form.age.data
            gender = form.gender.data
            pulse_rate = form.pulse_rate.data    
            systolic_bp = form.systolic_bp.data
            diastolic_bp = form.diastolic_bp.data   
            glucose = form.glucose.data
            height = form.height.data
            weight = form.weight.data
            family_diabetes = form.family_diabetes.data
            hypertensive = form.hypertensive.data   
            family_hypertension = form.family_hypertension.data
            cardiovascular_disease = form.cardiovascular_disease.data
            stroke = form.stroke.data
            
            
            return redirect(url_for('user.dashboard'))
    
    
    return render_template("data_entry.html", title="Data Entry")

@bp.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template("dashboard.html", title="Dashboard")

