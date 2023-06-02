from app.extensions import ns
from flask_restx import Resource, Namespace
from app.models.course import Course
from app.Models.course_mod import course_model,course_input_model
from app.extensions import db
# ns = Namespace('Mansy')
@ns.route('/courses')
class courseAPI(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()
    

    @ns.expect(course_input_model)
    @ns.marshal_with(course_model)
    def post(self):
        print(ns.payload)
        course = Course(name=ns.payload['name'])
        db.session.add(course)
        db.session.commit()
        return course, 201

@ns.route('/courses/<int:id>')
class IdCourseAPI(Resource):
    
    @ns.marshal_with(course_model)
    def get(self,id):
        course = Course.query.get(id)
        return course
    
    @ns.marshal_with(course_model)
    @ns.expect(course_input_model)
    def put(self,id):
        course = Course.query.get(id)
        course.name = ns.payload['name']
        db.session.commit()
        return course
    
    def delete(self,id):
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return {}, 204