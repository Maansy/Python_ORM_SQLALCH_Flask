from flask import Flask
from .extensions import api, db, jwt
from app.apis.say_hello import *
from app.apis.course_api import *
from app.apis.student_api import *
from app.apis.user_api import *

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['JWT_SECRET_KEY'] = 'thisissecretkey'
    api.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    api.add_namespace(ns)
    return app