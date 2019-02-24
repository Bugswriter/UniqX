from datetime import datetime
from UniQx import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    profile = db.relationship('Profile', backref='profile_owner', uselist=False)

    def __repr__(self):
        return f"User('{ self.username }', '{ self.email }', '{ self.image_file }')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    image = db.Column(db.String(20), nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{ self.title }', '{ self.date }', '{ self.content }', '{ self.user_id }')"


class Profile(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    dob = db.Column(db.Date, nullable=False)
    country = db.Column(db.String, nullable=False)
    cover = db.Column(db.String(20), nullable=False, default='cover.jpg')
    
    def __repr__(self):
        return f"Profile( '{self.name }', '{ self.dob }', '{ self.country }')"
