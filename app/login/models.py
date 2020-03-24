from app import db
from datetime import datetime, date

class Login(db.Model):
    __tablename__ = 'login'

    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.String(30), nullable = False)

    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = db.relationship('Person', foreign_keys = person_id)

    #Action DateTime
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())  #Created at
    updated_at = db.Column(db.DateTime, nullable = True, default = None)  #Updated at
    deleted = db.Column(db.Boolean, default = 0)  #Deleted(soft delete)
    deleted_at = db.Column(db.DateTime, nullable = True, default = None)  #Deleted at(soft delete)

    def __init__(self, username, password, person_id, created_at, updated_at, deleted, deleted_at):
        self.username = username
        self.password = password
        self.person_id = person_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted = deleted
        self.deleted_at = deleted_at
    
    def __repr__(self):
        return 'Username: {}'.format(self.username)