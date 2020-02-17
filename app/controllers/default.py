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
    return "Deletado"
