from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func 

class User(db.Model,UserMixin):
    user_id = db.Column(db.String(8),primary_key=True)
    user_email = db.Column(db.String(30),unique=True)
    user_name = db.column(db.String(150))
    password = db.Column(db.String(150))
    user_type = db.column(db.String(10))
    scores = db.relationship('Score')

class Score(db.Model):
    score_id = db.Column(db.Integer,primary_key=True)
    score_value = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))

