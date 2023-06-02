from flask_restx import fields
from app.extensions import api
# from .student_mod import student_model

course_model = api.model('Course',{
    'id': fields.Integer,
    'name': fields.String,
    # 'students': fields.List(fields.Nested(student_model))
})


course_input_model = api.model('CourseInput',{
    'name' : fields.String,
})