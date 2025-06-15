from app.auth  import bp
from flask import render_template,request,session,redirect,url_for,flash
from app.auth.authenticator import Signup,Login
from app.extensions import db
from app.db_models.auth import User

@bp.route('/signup',methods=["GET","POST"])
def signup():
    form = Signup()
    if request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            phone = form.phone.data
            password = form.password.data
            
            # Check if user already exists
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash("Email already registered. Please use a different email.", "danger")
                return redirect(url_for("auth.login"))

            # Create new user
            new_user = User(user_name=username, password=password,email=email,phone_number=phone)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            
            #user session requirements
            session["user_id"] = new_user.id
            session["user_name"] = new_user.user_name
            
            return redirect(url_for("user.dashboard")) 
        
    return render_template("signup.html", title="SignUp",form=form)   

  
@bp.route('/login', methods=["GET","POST"])
def login():
    form = Login()
    if request.method == "GET":
        session.clear()
        return render_template("login.html",title="Login",form=form) 
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session["user_id"] =   user.id
            session["user_name"] = user.user_name
            return redirect(url_for("user.dashboard"))
    
    return render_template("login.html",title="Login",form=form)      
            
