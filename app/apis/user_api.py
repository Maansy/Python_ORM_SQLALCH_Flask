from app.extensions import ns, db
from flask_restx import Resource
from flask_jwt_extended import create_access_token, current_user
from app.models.user import User 
from app.Models.user_mod import user_model,login_model
from werkzeug.security import generate_password_hash, check_password_hash

@ns.route('/register')
class userAPI(Resource):
    @ns.doc(security='jsonWebToken')
    @ns.expect(login_model)
    @ns.marshal_with(user_model)
    def post(self):
        user = User(name=ns.payload['name'], \
                                password = generate_password_hash(ns.payload['password']))
        # print(type(user.password))
        db.session.add(user)
        db.session.commit()
        return user, 201
    
@ns.route('/login')
class Login(Resource):
    
    @ns.expect(login_model)
    def post(self):
        user = User.query.filter_by(name=ns.payload['name']).first()
        if not user:
             return {'Error': 'User does not exist'}, 401
        if not check_password_hash(user.password,ns.payload['password']):
            return {'error':'Wrong password'}, 401
        return {'access Token':create_access_token(user)}