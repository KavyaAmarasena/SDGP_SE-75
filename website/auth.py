from flask import Blueprint,render_template,request,flash
from .models import User 
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint('auth',__name__)

# This is the app route to the login method 
@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        data = request.form
        print(data)
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(user_id=username).first()

        if(user):
            if check_password_hash(user.password,password):
                print("Logged In Successfully !")
            else:
                print("Incorrect Password !")
        else:
            print("User does not exist !")

    return render_template("login.html",form_type="sign-in-form")

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/login#",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email= request.form.get('email')
        password = request.form.get('password')

        print(first_name)
        print(last_name)
        print(email)
        print(password)

    return render_template("login.html",form_type="sign-up-form")
