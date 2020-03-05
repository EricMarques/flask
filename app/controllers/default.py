from flask import render_template, request, redirect
from app import app, db
from datetime import datetime

from app.models.tables import Person, BloodType
from app.models.forms import LoginForm, PersonRegistrationForm, BloodTypeForm


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        print(login.username.data)
        print(login.password.data)
    else:
        print(login.errors)
    return render_template('login.html', login=login)


@app.route('/test', methods=['GET'])
def Blood():
    bloodType = BloodTypeForm()
    blood_Type = BloodType.query.filter_by().all()
    
    return render_template('test.html',bloodType=blood_Type)

@app.route('/personRegister', methods=['POST', 'GET', 'PUT'])
def Person():
    personRegistration = PersonRegistrationForm()
    #Person Identification
    document_type = personRegistration.document_type.data  #0 - PF || 1 - PJ
    registration_card = personRegistration.registration_card.data  #CPF/CNPJ
    first_name = personRegistration.first_name.data  #Name
    second_name = personRegistration.second_name.data  #Second name
    birth_day = personRegistration.birth_day.data  #Birth day
    nick_name = personRegistration.nick_name.data  #Nickname
    identification =  personRegistration.identification.data  #Identification
    father_name = personRegistration.father_name.data  #Father name
    mother_name = personRegistration.mother_name.data  #Mother name
    #Contact
    email = personRegistration.email.data  #E-mail
    phone_number = personRegistration.phone_number.data  #Phone
    cellphone_number = personRegistration.cellphone_number.data  #Cell phone

    #Address
    postal_code = personRegistration.postal_code.data  #Postal code
    street = personRegistration.street.data  #Street
    number = personRegistration.number.data  #Numer
    complement = personRegistration.complement.data  #Complement
    neighborhood = personRegistration.neighborhood.data  #Neighborhood
    city = personRegistration.city.data  #City
    state = personRegistration.state.data  #State
    country = personRegistration.country.data  #Country

    #Observations
    observations = personRegistration.observations.data

    #Action DateTime
    created_at = datetime.now()  #Created at
    updated_at = None  #Updated at  #Deleted(soft delete)
    deleted = 0  #Deleted(soft delete)
    deleted_at = None  #Deleted at(soft delete)

    print('NO MÉTODO => Fields - document_type: {} -> registration_card: {} -> first_name: {} -> second_name: {} -> birth_day: {} -> nick_name: {} -> identification: {} -> father_name: {} -> mother_name: {} -> email: {} -> phone_number: {} -> cellphone_number: {} -> postal_code: {} -> street: {} -> number: {} -> complement: {} -> neighborhood: {} -> city: {} -> state: {} -> country: {} -> observations: {} -> created_at: {} -> updated_at: {} -> deleted: {} -> deleted_at: {}'.format(document_type, registration_card, first_name, second_name, birth_day, nick_name, identification, father_name, mother_name, email, phone_number, cellphone_number, postal_code, street, number, complement, neighborhood, city, state, country, observations, created_at, updated_at, deleted, deleted_at))


    if personRegistration.validate_on_submit():
        print('ANTES DE SALVAR => Fields - document_type: {} -> registration_card: {} -> first_name: {} -> second_name: {} -> birth_day: {} -> nick_name: {} -> identification: {} -> father_name: {} -> mother_name: {} -> email: {} -> phone_number: {} -> cellphone_number: {} -> postal_code: {} -> street: {} -> number: {} -> complement: {} -> neighborhood: {} -> city: {} -> state: {} -> country: {} -> observations: {} -> created_at: {} -> updated_at: {} -> deleted: {} -> deleted_at: {}'.format(document_type, registration_card, first_name, second_name, birth_day, nick_name, identification, father_name, mother_name, email, phone_number, cellphone_number, postal_code, street, number, complement, neighborhood, city, state, country, observations, created_at, updated_at, deleted, deleted_at))

        new_person = Person(document_type=document_type, registration_card=registration_card, first_name=first_name, second_name=second_name, birth_day=birth_day, nick_name=nick_name, identification=identification, father_name=father_name, mother_name=mother_name, email=email, phone_number=phone_number, cellphone_number=cellphone_number, postal_code=postal_code, street=street, number=number, complement=complement, neighborhood=neighborhood, city=city, state=state, country=country, observations=observations, created_at=created_at, updated_at=updated_at, deleted=deleted, deleted_at=deleted_at)

        new = Person(document_type=document_type,)

        db.session.add(new_person)
        db.session.commit()

        print('DEPOIS DE SALVAR => OTHER FIELDS:\ndocument_type: {} -> registration_card: {} -> first_name: {} -> second_name: {} -> birth_day: {} -> nick_name: {} -> identification: {} -> father_name: {} -> mother_name: {} -> email: {} -> phone_number: {} -> cellphone_number: {} -> postal_code: {} -> street: {} -> number: {} -> complement: {} -> neighborhood: {} -> city: {} -> state: {} -> country: {} -> observations: {} -> created_at: {} -> updated_at: {} -> deleted: {} -> deleted_at: {}'.format(document_type, registration_card, first_name, second_name, birth_day, nick_name, identification, father_name, mother_name, email, phone_number, cellphone_number, postal_code, street, number, complement, neighborhood, city, state, country, observations, created_at, updated_at, deleted, deleted_at))

        return redirect('../templates/index.html')
    else:
        #return personRegistration.errors
        print(personRegistration.errors)
    
    return render_template('person/personRegister.html', personRegistration = personRegistration)


'''
*****************
@app.route('/testSelect/<name>')
@app.route('/testSelect', defaults={"name": None})
def testSelect(name):
    #select = User.query.filter_by(username="erc_m").all() #retorna o usuário por campo 
    select = User.query.filter_by(username="erc_m").first() #retorna registro por ID
    print(select)
    return render_template('test.html', name = select.name)

@app.route('/testUpdate/<info>')
@app.route('/testUpdate', defaults={"info": None})
def testUpdate(info):
    update = User.query.filter_by(username="erc_m").first()
    update.name = "Eric F. Marques"
    db.session.add(update)
    db.session.commit()
    return "Alterado"

@app.route('/testDelete/<info>')
@app.route('/testDelete', defaults={"info": None})
def testDelete(info):
    delete = User.query.filter_by(username="ercic").first()
    db.session.delete(delete)
    db.session.commit()
    return "Deletado" '''
