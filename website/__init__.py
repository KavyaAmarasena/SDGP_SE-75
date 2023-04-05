from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

app = Flask(__name__)    

def create_app():
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learnly.db'
    app.config['SECRET_KEY'] = '706a1ea0ba514612a43dd4d736908671'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .api import api

    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")
    app.register_blueprint(api,url_prefix="/api")

    # from .models import Student,Teacher

    create_database(app)

    return app 


def create_database(app):
    if not path.exists("instance/learnly.db"):
        with app.app_context():
            db.create_all()
        print("Created Database !")
    else:
        print("Already created DB")

