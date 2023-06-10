from flask_restx import fields
from app.extensions import api

user_model = api.model('User',{
    'id' : fields.Integer,
    'name': fields.String,
})

login_model = api.model('Login',{
    'name': fields.String,
    'password': fields.String,
})