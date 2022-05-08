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

class Pitch(db.Model):
    '''
    This class will contain the database schema for picthes table
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String)
    category = db.Column(db.String)
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref='pitch',lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

class Comment(db.Model):
    '''
    This class will contain the schema for comments
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()
        return comments

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    