from flask_restx import Resource,Namespace
from app.extensions import ns

# ns = Namespace('Mansy')
@ns.doc(security='jsonWebToken')
@ns.route('/hello')
class Hello(Resource):
    def get(self):
        return {'hey':'Mansy is here'}