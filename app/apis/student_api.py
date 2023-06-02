from app.extensions import ns, db
from flask_restx import Resource
from app.models.student import Student
from app.Models.student_mod import student_model,student_input_model

# ns = Namespace('Mansy')
@ns.route('/student')
class courseAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()
    
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def post(self):
        student = Student(name=ns.payload['name'], \
                             course_id = ns.payload['course_id'])
        db.session.add(student)
        db.session.commit()
        return student, 201
        