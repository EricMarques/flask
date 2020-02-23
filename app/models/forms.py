from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, DateField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class PersonRegistrationForm(FlaskForm):
    #Person Identification
    document_type = RadioField("Tipo de Pessoa", choices=[(1,'Pessoa Física'), (0, 'Pessoa Jurídica')], default=1)
    registration_card = StringField("", validators=[DataRequired()])
    first_name = StringField("Nome", validators=[DataRequired()])
    second_name = StringField("Sobrenome", validators=[DataRequired()])
    birth_day = DateField("Dt. Nascimento")
    nick_name = StringField("Apelido")
    identification = StringField("Identidade")
    father_name = StringField("Nome do pai")
    mother_name = StringField("Nome da mãe")

    #Contact
    email = StringField("E-mail", validators=[DataRequired()], description="seu.email@seu.dominio")
    phone_number = StringField("Telefone")
    cellphone_number = StringField("Celular", validators=[DataRequired()])

    #Address
    postal_code = StringField("CEP")
    street = StringField("Logradouro")
    number = StringField("Número")
    complement = StringField("Complemento")
    neighborhood = StringField("Bairro")
    city = StringField("Cidade")
    state = StringField("Estado")
    country = StringField("País")

    #Observations
    observations = TextAreaField("Observações")

    #Buttons
    submit = SubmitField("Salvar")
    cancel = SubmitField("Cancelar")