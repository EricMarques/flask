# Criação de tabelas necessárias que não possuirão interfaces
# As tabelas que terão interfaces devem ser criadas nos 'models' dos módulos
from app import db
from datetime import datetime, date


class BloodType(db.Model):
    __tablename__ = 'blood_types'

    id = db.Column(db.Integer, primary_key = True)
    #Blood Type
    blood_type = db.Column(db.String(7), unique = True, nullable = False)  #Blood Type

    def __init__(self, blood_type):
        self.blood_type = blood_type
    
    def __repr__(self):
        return '{}'.format(self.blood_type)


class  Ethnicitie(db.Model):
    __tablename__ = 'ethnicities'
    #Ethnicitie
    id = db.Column(db.Integer, primary_key = True)
    ethnicity = db.Column(db.String(14), nullable = False)  #Ethnicity

    def __init__(self, ethnicitie):
        self.ethnicity = ethnicitie

    def __repr__(self):
        return 'Ethnicitie: {}'.format(self.ethnicity)
        
'''
class NameClass(db.Model):
    __tablename__ = 'table_name'
    #Fields
    id = db.Column(db.Integer, primary_key = True)
    field_name = db.Column(db.String(50), nullable = False)  #Field_name

    #Action DateTime
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())  #Created at
    updated_at = db.Column(db.DateTime, nullable = True, default = None)  #Updated at
    deleted = db.Column(db.Boolean, default = 0)  #Deleted(soft delete)
    deleted_at = db.Column(db.DateTime, nullable = True, default = None)  #Deleted at(soft delete)

    def __init__(self, created_at, updated_at, deleted, deleted_at):
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted = deleted
        self.deleted_at = deleted_at
    
    def __repr__(self):
        return 'Field_name: {}'.format(self.field_name)
'''