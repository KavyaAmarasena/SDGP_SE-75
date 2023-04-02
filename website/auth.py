from flask import Blueprint,render_template,request,redirect
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
            if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
                username = request.form['username']
                password = request.form['password']

            # Check if account exists using SQLite database
                conn = sqlite3.connect('./instance/learnly.db')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM Student WHERE (username = ? OR email = ?) AND password = ?',
                           (username, username, password,))
                account = cursor.fetchone()

            # If account exists in user details table in our database
            if account:
                session['loggedin'] = True
                session['id'] = account[0]
                session['username'] = account[1]

                # Redirect to home page
                return redirect(url_for('SHome.html'))
            else:
                # Account doesn't exist or username/password is incorrect
                print('Incorrect username/password!')

            # Close connection and cursor
            cursor.close()
            conn.close()
    
    return render_template('login_student.html')




@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

