from flask import Blueprint,render_template,redirect,url_for
from website.auth import session

views = Blueprint('views',__name__)

@views.route("/")
def home():
    return render_template("homepage.html");


@views.route("/homepage-student")
def dashboard_student():
    if session.get('logged_in'):
        print(session)
        print("The session is logged!")
        return render_template("homepage_student.html")
    else:
        return redirect(url_for("auth.login_student"))

@views.route("/homepage-teacher/<tchr_id>")
def dashboard_teacher(tchr_id):
    return render_template("homepage_teacher.html")

@views.route("/logout")
def logout():
    session.pop("logged_in",None)
    return redirect(url_for("views.home"))