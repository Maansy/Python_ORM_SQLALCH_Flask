from app.extensions import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),unique = True)
    instuctor_id = db.Column(db.ForeignKey('user.id'))

    
    students = db.relationship('Student',back_populates='course')
    instuctor = db.relationship('User',back_populates='courses')