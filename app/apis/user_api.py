from app.extensions import ns, db
from flask_restx import Resource
from app.models.user import User 
from app.Models.user_mod import user_model,login_model
from werkzeug.security import generate_password_hash, check_password_hash

@ns.route('/register')
class userAPI(Resource):
    @ns.expect(login_model)
    @ns.marshal_with(user_model)
    def post(self):
        user = User(name=ns.payload['name'], \
                                password = generate_password_hash(ns.payload['password']))
        # print(type(user.password))
        db.session.add(user)
        db.session.commit()
        return user, 201