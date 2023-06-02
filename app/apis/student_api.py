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
    
@ns.route('/student/<int:id>')
class IdStudentAPI(Resource):
    
    @ns.marshal_with(student_model)
    def get(self,id):
        student = Student.query.get(id)
        return student
    
    @ns.marshal_with(student_model)
    @ns.expect(student_input_model)
    def put(self,id):
        student = Student.query.get(id)
        student.name = ns.payload['name']
        student.course_id = ns.payload['course_id']
        db.session.commit()
        return student
    
    def delete(self,id):
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return {}, 204
