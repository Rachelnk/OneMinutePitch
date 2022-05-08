from . import db
from werkzeug.security import generate_password_hash,check_password_hash
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref='user',lazy = 'dynamic')
    comments = db.relationship('Comment',backref='user',lazy='dynamic')

    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

    