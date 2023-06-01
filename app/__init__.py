from flask import Flask
from extensions import api, db
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    api.__init__(app)
    db.__init__(app)

    return app