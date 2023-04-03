from flask import Blueprint,render_template,request,redirect,session,url_for,flash
from flask_sqlalchemy import SQLAlchemy
import jwt
import sqlite3
from sqlite3 import Error
from datetime import datetime,timedelta
from .models import Teacher,Student 
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint('auth',__name__)

# This is the app route to the login method 
@auth.route("/login-teacher",methods=['GET','POST'])
def login_teacher():
    # if request.method == "POST":
    #     data = request.form
    #     print(data)
    #     username = request.form.get('username')
    #     password = request.form.get('password')

    #     user = User.query.filter_by(user_id=username).first()

    #     if(user):
    #         if check_password_hash(user.password,password):
    #             print("Logged In Successfully !")
    #         else:
    #             print("Incorrect Password !")
    #     else:
    #         print("User does not exist !")

    return render_template("login_teacher.html")


@auth.route("/login-student",methods=['GET','POST'])
def login_student():
    if(request.method == "POST"):
            with sqlite3.connect("./instance/learnly.db") as con:
                username = request.form['username']
                password = request.form['password']
                print(password)
                print(type(password))
            # Check if account exists using SQLite database
                cursor = con.cursor()
                try:
                # cursor.execute('SELECT * FROM Student WHERE (std_id = ? OR std_email = ?)',
                #            (username, username))
                    cursor.execute('SELECT std_pass FROM Student WHERE (std_id = ? OR std_email = ?)',(username,username))

                    std_password_hash_list = cursor.fetchall()
                    print(type(std_password_hash_list))

                    #the std_password_has is a tuple
                    std_password_hash = std_password_hash_list[0]
                    #In order to use check_password_hash we need to get the string of the std_password_hash tuple
                    std_password_hash_str =  ''.join(map(str,std_password_hash))

                    print(std_password_hash)
                    print(type(std_password_hash))

                    print(std_password_hash_str)

                    if(check_password_hash(std_password_hash_str,password)):
                        return redirect(url_for('views.dashboard_student'))
                    else:
                        flash("Incorrect username/password")
                        print("Incorrect username/password")
                       

                except Error as e:
                    print(e)
            
            cursor.close()
            con.close()

            # If account exists in user details table in our database
            # if account:
            #     session['loggedin'] = True
            #     session['id'] = account[0]
            #     session['username'] = account[1]

                # Redirect to home page
                
            # else:
                # Account doesn't exist or username/password is incorrect
                # print('Incorrect username/password!')

            # Close connection and cursor
                
    
    return render_template('login_student.html')


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

