from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, DateField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class PersonRegistrationForm(FlaskForm):
    #Person Identification
    document_type = RadioField("Tipo de Pessoa", choices=[(0,'Pessoa Física'), (1, 'Pessoa Jurídica')], validators=False, default = 0)
    registration_card = StringField("", validators=[DataRequired(), Length(max=15)])
    first_name = StringField("Nome", validators=[DataRequired()])
    second_name = StringField("Sobrenome", validators=[DataRequired()])
    birth_day = DateField("Dt. Nascimento", default=None)
    nick_name = StringField("Apelido", validators=[Length(max=20)], default=None)
    identification = StringField("Identidade", validators=[Length(max=20)], default=None)
    father_name = StringField("Nome do pai", validators=[Length(max=100)], default=None)
    mother_name = StringField("Nome da mãe", validators=[Length(max=100)], default=None)

    #Contact
    email = StringField("E-mail", validators=[DataRequired(), Email(message="Formato de e-mail incorreto!")])
    phone_number = StringField("Telefone", validators=[Length(max=10)], default=None)
    cellphone_number = StringField("Celular", validators=[DataRequired(), Length(max=11)])

    #Address
    postal_code = StringField("CEP", validators=[Length(max=8)], default=None)
    street = StringField("Logradouro", validators=[Length(max=50)], default=None)
    number = StringField("Número", validators=[Length(max=10)], default=None)
    complement = StringField("Complemento", validators=[Length(max=50)], default=None)
    neighborhood = StringField("Bairro", validators=[Length(max=50)], default=None)
    city = StringField("Cidade", validators=[Length(max=50)], default=None)
    state = StringField("Estado", validators=[Length(max=50)], default=None)
    country = StringField("País", validators=[Length(max=40)], default=None)

    #Observations
    observations = TextAreaField("Observações", validators=[Length(max=400)], default=None)

    #Buttons
    submit = SubmitField("Salvar")
    cancel = SubmitField("Cancelar")