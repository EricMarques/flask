from flask import Blueprint, render_template, request, redirect
from app import db
from app.person.models import Person
from app.person.forms import PersonRegistrationForm

from datetime import datetime, date

person_blueprint = Blueprint('person', __name__)

@person_blueprint.route('/person', methods=['POST', 'GET'])
def person():
    personRegistration = PersonRegistrationForm()

    if request.method == 'POST':
        print('POST')
    else:
        print('Não POST')
    number = personRegistration.number.data  #Number
    print(type(number))
    if number == '' or number == 'sn':
        number = 0
    print("BD -> {}" .format(number))
    if personRegistration.validate_on_submit():
        #Person Identification
        document_type = personRegistration.document_type.data  #0 - PF || 1 - PJ
        registration_card = personRegistration.registration_card.data  #CPF/CNPJ
        identification =  str.upper(personRegistration.identification.data)  #Identification
        if identification == '':
            identification = None
        first_name = str.upper(personRegistration.first_name.data)  #Name
        second_name = str.upper(personRegistration.second_name.data)  #Second name
        birth_day = personRegistration.birth_day.data  #Birth day
        if birth_day == '':
            birth_day = datetime(1900, 1, 1).date()
        nick_name = str.upper(personRegistration.nick_name.data)  #Nickname
        if nick_name == '':
            nick_name = None
        father_name = str.upper(personRegistration.father_name.data)  #Father name
        if father_name == '':
            father_name = None
        mother_name = str.upper(personRegistration.mother_name.data)  #Mother name
        if mother_name == '':
            mother_name = None
        #Contact
        email = str.lower(personRegistration.email.data)  #E-mail
        phone_number = personRegistration.phone_number.data  #Phone
        if phone_number == '':
            phone_number = None
        cellphone_number = personRegistration.cellphone_number.data  #Cell phone

        #Address
        postal_code = personRegistration.postal_code.data  #Postal code
        if postal_code == '':
            postal_code = None
        street = str.upper(personRegistration.street.data)  #Street
        if street == '':
            street = None
        number = str.upper(personRegistration.number.data)  #Number
        if number == 'SN' or number == '':
            number = 0
        complement = str.upper(personRegistration.complement.data)  #Complement
        if complement == '':
            complement = None
        neighborhood = str.upper(personRegistration.neighborhood.data)  #Neighborhood
        if neighborhood == '':
            neighborhood = None
        city = str.upper(personRegistration.city.data)  #City
        if city == '':
            city = None
        state = str.upper(personRegistration.state.data)  #State
        if state == '':
            state = None
        country = str.upper(personRegistration.country.data)  #Country
        if country == '':
            country = None

        #Observations
        observations = personRegistration.observations.data
        if observations == '':
            observations = None

        #Action DateTime
        created_at = datetime.now()  #Created at
        updated_at = None  #Updated at  #Deleted(soft delete)
        deleted = 0  #Deleted(soft delete)
        deleted_at = None  #Deleted at(soft delete)

        print('BD: {} -> NN: {}'.format(birth_day, nick_name))
        new_person = Person(document_type=document_type, registration_card=registration_card, first_name=first_name, second_name=second_name, birth_day=birth_day, nick_name=nick_name, identification=identification, father_name=father_name, mother_name=mother_name, email=email, phone_number=phone_number, cellphone_number=cellphone_number, postal_code=postal_code, street=street, number=number, complement=complement, neighborhood=neighborhood, city=city, state=state, country=country, observations=observations, created_at=created_at, updated_at=updated_at, deleted=deleted, deleted_at=deleted_at)

        db.session.add(new_person)
        db.session.commit()
        # Criar listagem e fazer redirecionamento para ela.
        return redirect('../')
    else:
        #return personRegistration.errors
        print(personRegistration.errors)
    
    return render_template('person/form/personRegister.html', personRegistration = personRegistration)