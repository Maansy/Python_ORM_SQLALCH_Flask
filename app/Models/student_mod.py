from flask_restx import fields
from app.extensions import api
from .course_mod import course_model


student_model = api.model('Student',{
    'id': fields.Integer,
    'name': fields.String,
    'course': fields.Nested(course_model),
})

student_input_model = api.model('StudetnIn',{
    'name':fields.String,
    'course_id':fields.Integer
})