from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(20), nullable = True)
    name = db.Column(db.String(50), nullable = True)
    email = db.Column(db.String(120), unique = True, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.now())

    def __init__(self, username, password, name, email, created_at):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.created_at = created_at

    def __repr__(self):
        return '<User %r>' % self.username
    
class Post(db.Model):
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User', foreign_keys = user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % self.post_id

class Follow(db.Model):
    __tablename__ = 'follows'

    follow_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User', foreign_keys = user_id)
    follower = db.relationship('User', foreign_keys = follower_id)

    def __init__(self, user_id, follower_id):
        self.user_id = user_id
        self.follower_id = follower_id