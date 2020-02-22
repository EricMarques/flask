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


class BloodType(db.Model):
    __tablename__ = 'blood_types'

    id = db.Column(db.Integer, primary_key = True)
    #Blood Type
    blood_type = db.Column(db.String(7), unique = True, nullable = False)  #Blood Type

    def __init__(self, blood_type):
        self.blood_type = blood_type
    
    def __repr__(self):
        return 'Blood Type: ' + self.blood_type


class PersonBloodType(db.Model):
    __tablename__ = 'person_blood_types'

    id = db.Column(db.Integer, primary_key = True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable = False)  #Person id
    blood_type_id = db.Column(db.Integer, db.ForeignKey('blood_types.id'), nullable = False)  #Blood type id

    person = db.relationship('Person', foreign_keys = person_id)
    blood_type = db.relationship('BloodType', foreign_keys = blood_type_id)

    def __init__(self, person_id, blood_type_id):
        self.person = person_id
        self.blood_type = blood_type_id


class  Ethnicitie(db.Model):
    __tablename__ = 'ethnicities'
    #Ethnicitie
    id = db.Column(db.Integer, primary_key = True)
    ethnicity = db.Column(db.String(14), nullable = False)  #Ethnicity

    def __init__(self, ethnicitie):
        self.ethnicity = ethnicitie

    def __repr__(self):
        return 'Ethnicitie: ' + self.ethnicity
        

class PersonEthnicity(db.Model):
    __tablename__ = 'person_ethnicities'

    id = db.Column(db.Integer, primary_key = True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable = False)  #Person id
    ethnicitie_id = db.Column(db.Integer, db.ForeignKey('ethnicities.id'), nullable = False)  #Ethnicitie id

    person = db.relationship('Person', foreign_keys = person_id)
    ethnicitie = db.relationship('Ethnicitie', foreign_keys = ethnicitie_id)

    def __init__(self, person_id, ethnicitie_id):
        self.person_id = person_id
        self.ethnicitie_id = ethnicitie_id


class Religion(db.Model):
    __tablename__ = 'religions'
    #Religion
    id = db.Column(db.Integer, primary_key = True)
    religion = db.Column(db.String(50), nullable = False)  #Religion

    def __init__(self, religion):
        self.religion = religion
    
    def __repr__(self):
        return 'Religion: ' + self.religion


class PersonReligion(db.Model):
    __tablename__ = 'person_religion'

    id = db.Column(db.Integer, primary_key = True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable = False)  #Person id
    religion_id = db.Column(db.Integer, db.ForeignKey('religions.id'), nullable = False)  #Religion id

    person = db.relationship('Person', foreign_keys = person_id)
    religion = db.relationship('Religion', foreign_keys = religion_id)

    def __init__(self, person_id, religion_id):
        self.person_id = person_id
        self.religion_id = religion_id