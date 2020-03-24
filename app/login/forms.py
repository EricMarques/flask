from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    #username
    username = StringField('username', validators=[DataRequired()])
    #Password
    password = PasswordField('password', validators=[DataRequired()])
    #Remember me
    remember_me = BooleanField('remember_me')

    #Submit
    submit = SubmitField('Entrar')