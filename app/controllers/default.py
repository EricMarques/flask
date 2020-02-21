from flask import render_template, request, redirect
from app import app, db
from datetime import datetime

from app.models.tables import Person
from app.models.forms import LoginForm, PersonRegistrationForm


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

@app.route('/personRegister', methods=['GET', 'POST'])
def Person():
    personRegistration = PersonRegistrationForm()
    '''
    self.document_type = document_type
        self.registration_card = registration_card
        self.first_name = first_name
        self.second_name = second_name
        self.birth_day = birth_day
        self.nick_name = nick_name
        self.identification = identification
        self.email = email
        self.phone_number = phone_number
        self.cellphone_number = cellphone_number
        self.father_name = father_name
        self.mother_name = mother_name
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
    '''
    person_name = personRegistration.name.data
    person_email = personRegistration.email.data
    created_at = datetime.now()
    updated_at = None
    deleted = 0
    deleted_at = None
    if personRegistration.validate_on_submit():
        new_person = Person(name=person_name, email=person_email, created_at=created_at, updated_at=updated_at, deleted=deleted, deleted_at=deleted_at)
        db.session.add(new_person)
        db.session.commit()

        print('name: {} -> email: {} -> criado em: {} -> modificado em: {} -> deletado: {} -> deletado em: {}'.format(person_name, person_email, created_at, updated_at, deleted, deleted_at))

        return redirect('/personRegister')
    else:
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