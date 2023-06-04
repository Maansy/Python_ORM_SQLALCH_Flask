from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Namespace
from flask_jwt_extended import JWTManager

authorizations = {
    'jsonWebToken': { # jwt is the name of the authorization
        'type': 'apiKey', # apiKey is the type of the authorization
        'in': 'header', # header is the location of the authorization
        'name': 'Authorization', # Authorization is the name of the authorization header
    }
}

api = Api()
db = SQLAlchemy()
ns = Namespace('Mansy', authorizations=authorizations)
jwt = JWTManager()
# count = 2
# fruit = 'apple'

# print(f'{count = }')
# print(f'{fruit = }')
