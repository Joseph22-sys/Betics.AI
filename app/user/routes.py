from app.user import bp
from flask import render_template,session, redirect, url_for,request
from app.user.data_validator import Userdata

@bp.route('/dataentry',methods=["GET"])
def dataentry():
    if 'username' not in session:
        return redirect(url_for('auth.signup'))
    
   
    form = Userdata()
    
    return render_template("data_entry.html", title="Data Entry",form=form)

@bp.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template("dashboard.html", title="Dashboard")

