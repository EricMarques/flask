from app import db
from datetime import datetime, date


class Religion(db.Model):
    __tablename__ = 'religions'
    #Religion
    id = db.Column(db.Integer, primary_key = True)
    religion = db.Column(db.String(50), nullable = False)  #Religion
    denomination = db.Column(db.String(70), nullable = True)  #Denomination

    #Observations
    observations = db.Column(db.String(500), nullable = True, default = None)  #Observations

    #Action DateTime
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())  #Created at
    updated_at = db.Column(db.DateTime, nullable = True, default = None)  #Updated at
    deleted = db.Column(db.Boolean, default = 0)  #Deleted(soft delete)
    deleted_at = db.Column(db.DateTime, nullable = True, default = None)  #Deleted at(soft delete)

    def __init__(self, religion, denomination, observations, created_at, updated_at, deleted, deleted_at):
        self.religion = religion
        self.denomination = denomination
        self.observations = observations
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted = deleted
        self.deleted_at = deleted_at
    
    def __repr__(self):
        return 'Religion: {}'.format(self.religion)