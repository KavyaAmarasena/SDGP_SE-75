from flask import Blueprint,render_template,request,redirect,session,url_for,flash,jsonify
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

                    if len(tchr_password_hash_list) ==0:
                        error_message = "Incorrect username or password ! Please try again"
                        return render_template("login_teacher.html",error_message = error_message)


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

                        cursor.execute('SELECT tchr_id,tchr_fname,tchr_lname FROM Teacher WHERE (tchr_id = ? OR tchr_email = ?)',(username,username))

                        tchr_details = cursor.fetchall()
                        tchr_info = list(tchr_details[0])

                        session['user_type'] = 'teacher'
                        session["logged_in"] = True
                        session["tchr_id"] = tchr_info[0]
                        session["tchr_fname"] = tchr_info[1]
                        session["tchr_lname"] = tchr_info[2]
                        
                        token = create_token(tchr_info[0],tchr_info[1],tchr_info[2])
                        session["token"] = token

                        return redirect(url_for('views.dashboard_teacher'))
                    else:
                        error_message = "Incorrect username or password ! Please try again"
                        return render_template("login_teacher.html",error_message = error_message)
                       
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

                    if len(std_password_hash_list) ==0:
                        error_message = "Incorrect username or password ! Please try again"
                        return render_template("login_student.html",error_message = error_message)

                    #the std_password_has is a tuple
                    std_password_hash = std_password_hash_list[0]
                    #In order to use check_password_hash we need to get the string of the std_password_hash tuple
                    std_password_hash_str =  ''.join(map(str,std_password_hash))

                    # This method performs to see if the password entered by the user matches the hash value
                    # that was stored in the database if its true then it redirects to the dashboard
                    if(check_password_hash(std_password_hash_str,password)):

                        cursor.execute('SELECT std_id,std_fname,std_lname FROM Student WHERE (std_id = ? OR std_email = ?)',(username,username))

                        std_details = cursor.fetchall()
                        std_info = list(std_details[0])
                        # std_id_str = ''.join(map(str,std_id))

                        # print(std_id[0])
                        # print(type(std_id))
                        session['user_type'] = 'student'
                        session["logged_in"] = True
                        session["std_id"] = std_info[0]
                        session["std_fname"] = std_info[1]
                        session["std_lname"] = std_info[2]
                        
                        token = create_token(std_info[0],std_info[1],std_info[2])
                        session["token"] = token

                        print(token)

                        print(std_details)

                        return redirect(url_for('views.dashboard_student'))
                    else:
                        error_message = "Incorrect username or password ! Please try again"
                        return render_template("login_student.html",error_message = error_message)
                       
                except Error as e:
                    print(e)
            
            cursor.close()
            con.close()
    
    return render_template('login_student.html')

@auth.route("/create-token")
def create_token(usr_id,usr_fname,usr_lname):
    token = jwt.encode({
          'user_id': usr_id,
          'usr_fname': usr_fname,
          'usr_lname': usr_lname
    },app.config['SECRET_KEY'],algorithm='HS256')

    return token

@auth.route('/logout')
def logout():
    # session['logged_in'] = False
    session.pop("logged_in",None)
    return redirect(url_for("views.home"))

@auth.route("/get-session")
def get_session():
    if session.get('logged_in'):
        user_type = session.get('user_type')

        if(user_type == 'student'):
            std_id = session.get('std_id')
            std_fname = session.get('std_fname')
            std_lname = session.get('std_lname')
            return jsonify({
                'user_type' : user_type,
                'std_id' : std_id,
                'std_fname' : std_fname,
                'std_lname' : std_lname
            })
        else:
            teacher_id = session.get('tchr_id')
            teacher_fname = session.get('tchr_fname')
            teacher_lname = session.get('tchr_lname')
            return jsonify({
                'user_type' : user_type,
                'teacher_id' : teacher_id,
                'teacher_fname' : teacher_fname,
                'teacher_lname' : teacher_lname
            })
        
    else:
        return redirect(url_for("views.home"))
