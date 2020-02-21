from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class PersonRegistrationForm(FlaskForm):
    #Person Identification
    document_type = RadioField("document_type")
    registration_card = StringField("registration_card", validators=[DataRequired()])
    first_name = StringField("first_name", validators=[DataRequired()])
    second_name = StringField("second_name", validators=[DataRequired()])
    birth_day = DateField("birth_day")
    nick_name = StringField("nick_name")
    identification = StringField("identification")
    father_name = StringField("father_name")
    mother_name = StringField("mother_name")

    #Contact
    email = StringField("email", validators=[DataRequired()])
    phone_number = StringField("phone_number")
    cellphone_number = StringField("cellphone_number", validators=[DataRequired()])

    #Address
    postal_code = StringField("postal_code")
    street = StringField("street")
    number = StringField("number")
    complement = StringField("complement")
    neighborhood = StringField("neighborhood")
    city = StringField("city")
    state = StringField("state")
    country = StringField("country")