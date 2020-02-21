from app import db
from datetime import datetime, date

class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key = True)
    #Person Identification
    document_type = db.Column(db.Boolean, nullable = False, default = 0)  #0 - PF || 1 - PJ
    registration_card = db.Column(db.String(15), unique = True, nullable = False)  #CPF/CNPJ
    first_name = db.Column(db.String(50), nullable = False)  #Name
    second_name = db.Column(db.String(100), nullable = False)  #Second name
    birth_day = db.Column(db.Date, nullable = True, default = None)  #Birth day
    nick_name = db.Column(db.String(20), nullable = True, default = None)  #Nickname
    identification = db.Column(db.String(15), nullable = True, default = None)  #Identification
    father_name = db.Column(db.String(100), nullable = True, default = None)  #Father name
    mother_name = db.Column(db.String(100), nullable = True, default = None)  #Mother name
    
    #Contact
    email = db.Column(db.String(120), unique = True, nullable = False)  #E-mail
    phone_number = db.Column(db.String(10), nullable = True, default = None)  #Phone
    cellphone_number = db.Column(db.String(10), nullable = False, default = None)  #Cell phone

    #Address
    postal_code = db.Column(db.String(7), nullable = True, default = None)  #Postal code
    street = db.Column(db.String(50), nullable = True, default = None)  #Street
    number = db.Column(db.Integer, nullable = True, default = 0)  #Numer
    complement = db.Column(db.String(50), nullable = True, default = None)  #Complement
    neighborhood = db.Column(db.String(50), nullable = True, default = None)  #Neighborhood
    city = db.Column(db.String(50), nullable = True, default = None)  #City
    state = db.Column(db.String(50), nullable = True, default = None)  #State
    country = db.Column(db.String(50), nullable = True, default = None)  #Country

    #Action DateTime
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())  #Created at
    updated_at = db.Column(db.DateTime, nullable = True, default = None)  #Updated at
    deleted = db.Column(db.Boolean, default = 0)  #Deleted(soft delete)
    deleted_at = db.Column(db.DateTime, nullable = True, default = None)  #Deleted at(soft delete)

    def __init__(self, document_type, registration_card, first_name, second_name, birth_day, nick_name, identification, father_name, mother_name, email, phone_number, cellphone_number, postal_code, street, number, complement, neighborhood, city, state, country, created_at, updated_at, deleted, deleted_at):
        self.document_type = document_type
        self.registration_card = registration_card
        self.first_name = first_name
        self.second_name = second_name
        self.birth_day = birth_day
        self.nick_name = nick_name
        self.identification = identification
        self.father_name = father_name
        self.mother_name = mother_name
        self.email = email
        self.phone_number = phone_number
        self.cellphone_number = cellphone_number
        self.postal_code = postal_code
        self.street = street
        self.number = number
        self.complement = complement
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.country = country
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted = deleted
        self.deleted_at = deleted_at

    def __repr__(self):
        return 'Person: ' + self.first_name + ' ' + self.second_name