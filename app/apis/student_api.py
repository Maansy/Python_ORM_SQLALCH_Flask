from app.extensions import ns
from flask_restx import Resource
from app.models.student import Student
from app.Models.student import student_model

# ns = Namespace('Mansy')
@ns.route('/student')
class courseAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()