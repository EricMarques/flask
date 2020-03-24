from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Required


class ReligionForm(FlaskForm):
    #Religion
    religion = StringField('Religião', validators=[DataRequired() ,Length(max=50)], default=None)
    #Denomination
    denomination = StringField('Denominação', validators=[Length(max=70)], default=None)
    #Observations
    observations = TextAreaField('Observações', validators=[Length(max=400)], default=None)
    
    #Buttons
    submit = SubmitField('Salvar')
    cancel = SubmitField('Cancelar')