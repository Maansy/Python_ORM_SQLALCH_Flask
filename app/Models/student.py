from flask_restx import fields
from app.extensions import api

student_model = api.model('Student',{
    'id': fields.Integer,
    'name': fields.String
    # 'students': ''
})