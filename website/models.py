from . import db
class Student(db.Model):
    std_id = db.Column(db.String(10),primary_key=True)
    std_fname = db.Column(db.String(40),nullable=False)
    std_lname = db.Column(db.String(40),nullable=False)
    std_email = db.Column(db.String(80),unique=True,nullable= False)
    std_pass = db.Column(db.String(40),nullable= False)

class Teacher(db.Model):
    tchr_id = db.Column(db.String(10),primary_key=True)
    tchr_fname = db.Column(db.String(40),nullable=False)
    tchr_lname = db.Column(db.String(40),nullable=False)
    tchr_email = db.Column(db.String(80),unique=True,nullable=False)
    tchr_pass = db.Column(db.String(40),nullable= False)



