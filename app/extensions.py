from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Namespace

api = Api()
db = SQLAlchemy()
ns = Namespace('Mansy')

# count = 2
# fruit = 'apple'

# print(f'{count = }')
# print(f'{fruit = }')
