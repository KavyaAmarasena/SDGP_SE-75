from flask import Blueprint,render_template,redirect,url_for
from website.auth import session

views = Blueprint('views',__name__)

@views.route("/")
def home():
    return render_template("home.html");


@views.route("/homepage-student")
def dashboard_student():
    if session.get('logged_in'):
        print(session)
        print("The session is logged!")
        return render_template("homepage_student.html")
    else:
        return redirect(url_for("auth.login_student"))

@views.route("/homepage-teacher")
def dashboard_teacher():
    if session.get('logged_in'):
        print(session)
        print("The session is logged!")
        return render_template("homepage_teacher.html")
    else:
        return redirect(url_for("auth.login_teacher"))


@views.route("/meeting")
def meet():
    return render_template("room.html")