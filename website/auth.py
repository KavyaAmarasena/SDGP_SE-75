from flask import Blueprint,render_template,request,redirect,session,url_for,flash,Flask
from flask_sqlalchemy import SQLAlchemy
import jwt
import sqlite3
from sqlite3 import Error
from datetime import datetime,timedelta
from .models import Teacher,Student 
from werkzeug.security import generate_password_hash,check_password_hash
from website import app

auth = Blueprint('auth',__name__)
app.config['SECRET_KEY'] = '706a1ea0ba514612a43dd4d736908671'

# This is the app route to the login method 
@auth.route("/login-teacher",methods=['GET','POST'])
def login_teacher():
    if(request.method == "POST"):
            with sqlite3.connect("./instance/learnly.db") as con:
                username = request.form['username']
                password = request.form['password']
                print(password)
                print(type(password))
            # Check if account exists using SQLite database
                cursor = con.cursor()
                try:
                    
                    # The query returns the password_hash where the student id or email equals to the name/email
                    # the user enters in the form
                    cursor.execute('SELECT tchr_pass FROM Teacher WHERE (tchr_id = ? OR tchr_email = ?)',(username,username))

                    #The fetchall() methods fetches all the data returned from the query 
                    tchr_password_hash_list = cursor.fetchall()

                    # print(type(std_password_hash_list))

                    #the std_password_has is a tuple
                    tchr_password_hash = tchr_password_hash_list[0]
                    #In order to use check_password_hash we need to get the string of the std_password_hash tuple
                    tchr_password_hash_str =  ''.join(map(str,tchr_password_hash))

                    # print(std_password_hash)
                    # print(type(std_password_hash))

                    # print(std_password_hash_str)

                    # This method performs to see if the password entered by the user matches the hash value
                    # that was stored in the database if its true then it redirects to the dashboard
                    if(check_password_hash(tchr_password_hash_str,password)):
                        return redirect(url_for('views.dashboard_teacher'))
                    else:
                        flash("Incorrect username/password")
                        print("Incorrect username/password")
                       
                except Error as e:
                    print(e)
            
            cursor.close()
            con.close()


    return render_template("login_teacher.html")


@auth.route("/login-student",methods=['GET','POST'])
def login_student():
    if(request.method == "POST"):
            with sqlite3.connect("./instance/learnly.db") as con:
                username = request.form['username']
                password = request.form['password']
                print(password)
                print(type(password))


                cursor = con.cursor()
                try:
                    
                    # The query returns the password_hash where the student id or email equals to the name/email
                    # the user enters in the form
                    cursor.execute('SELECT std_pass FROM Student WHERE (std_id = ? OR std_email = ?)',(username,username))

                    #The fetchall() methods fetches all the data returned from the query 
                    std_password_hash_list = cursor.fetchall()

                    #the std_password_has is a tuple
                    std_password_hash = std_password_hash_list[0]
                    #In order to use check_password_hash we need to get the string of the std_password_hash tuple
                    std_password_hash_str =  ''.join(map(str,std_password_hash))

                    # This method performs to see if the password entered by the user matches the hash value
                    # that was stored in the database if its true then it redirects to the dashboard
                    if(check_password_hash(std_password_hash_str,password)):

                        cursor.execute('SELECT std_id FROM Student WHERE (std_id = ? OR std_email = ?)',(username,username))

                        std_id_list = cursor.fetchall()
                        std_id = std_id_list[0]
                        std_id_str = ''.join(map(str,std_id))

                        session["logged_in"] = True
                        token = create_token(std_id_str)
                        print(token)

                        print(std_id_str)

                        return redirect(url_for('views.dashboard_student'))
                    else:
                        flash("Incorrect username/password")
                        print("Incorrect username/password")
                       
                except Error as e:
                    print(e)
            
            cursor.close()
            con.close()
    
    return render_template('login_student.html')

@app.route("/create-token")
def create_token(usr_id):
     token = jwt.encode({
          'user_id': usr_id
     },app.config['SECRET_KEY'],algorithm='HS256')

     return token

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

