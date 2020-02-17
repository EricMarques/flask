from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm


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




'''*****************'''
@app.route('/testInsert/<info>')
@app.route('/testInsert', defaults={"info": None})
def testInsert(info):
    insert = User('ercic', 'erc.m123', 'Eric F. B. Marques', 'erc.fbm@gmail.com')
    db.session.add(insert)
    db.session.commit()
    return "Inserido"

@app.route('/testSelect/<info>')
@app.route('/testSelect', defaults={"info": None})
def testSelect(info):
    #select = User.query.filter_by(username="erc_m").all() #retorna o usuário por campo 
    select = User.query.get(1) #retorna registro por ID
    print(select)
    return "%r" %select
