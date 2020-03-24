from flask import Blueprint, render_template, request, redirect
from app import db
from app.login.models import Login
from app.login.forms import LoginForm

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=["GET"])
def login():
    loginForm = LoginForm()
        
    if loginForm.validate_on_submit():
        print(loginForm.username.data)
        print(loginForm.password.data)
        if loginForm.remember_me.data == 1:
            print('ok')
        else:
            print('no')
    else:
        return render_template('404.html')

    return render_template('login/login.html', loginForm=loginForm)