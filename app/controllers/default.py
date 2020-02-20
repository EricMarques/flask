from flask import render_template, request, redirect
from app import app, db
from datetime import datetime

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

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        user_username = request.form['username']
        user_password = request.form['password']
        user_name = request.form['name']
        user_email = request.form['email']
        created_at = datetime.now()
        updated_at = None
        deleted = 0
        deleted_at = None
        new_user = User(username=user_username, password=user_password, name=user_name, email=user_email, created_at=created_at, updated_at=updated_at, deleted=deleted, deleted_at=deleted_at)
        db.session.add(new_user)
        db.session.commit()
        print('username: {} -> paswd: {} -> name: {} -> email: {} -> criado em: {} -> modificado em: {} -> deletado: {} -> deletado em: {}'.format(user_username, user_password, user_name, user_email, created_at, updates_at, deleted, deleted_at))
        return redirect('/user')
    else:
        return render_template('users/user.html')


'''
*****************
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
'''