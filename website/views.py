from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route("/")
def home():
    return render_template("homepage.html");


@views.route("/homepage-student")
def dashboard_student():
    return render_template("homepage_student.html")

@views.route("/homepage-teacher")
def dashboard_teacher():
    return render_template("homepage_teacher")
