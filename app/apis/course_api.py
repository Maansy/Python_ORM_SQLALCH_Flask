from app.extensions import ns
from flask_restx import Resource, Namespace
from app.models.course import Course
from app.Models.course import course_model

# ns = Namespace('Mansy')
@ns.route('/courses')
class courseAPI(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()