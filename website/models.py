from . import db
from werkzeug.security import generate_password_hash,check_password_hash
class Student(db.Model):
    std_id = db.Column(db.String(10),primary_key=True)
    std_fname = db.Column(db.String(40),nullable=False)
    std_lname = db.Column(db.String(40),nullable=False)
    std_email = db.Column(db.String(80),unique=True,nullable= False)
    std_pass = db.Column(db.String(256),nullable= False)

    @property
    def password(self):
        raise AttributeError ('Password is not a readable attribute !')
    
    @password.setter
    def password(self,password):
        self.std_password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.std_password_hash,password)

class Teacher(db.Model):
    tchr_id = db.Column(db.String(10),primary_key=True)
    tchr_fname = db.Column(db.String(40),nullable=False)
    tchr_lname = db.Column(db.String(40),nullable=False)
    tchr_email = db.Column(db.String(80),unique=True,nullable=False)
    tchr_pass = db.Column(db.String(256),nullable= False)



