# Query's de classes/tabelas que não possuirão interfaces
# Os formulários dverão ser criados nos 'forms' dos módulos
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from app.models.tables import BloodType

class BloodTypeForm(FlaskForm):
    def blood_choice():
        return BloodType.query.filter_by().all()
    blood_t = QuerySelectField("Tipo Sanguíneo", validators=[Required()], query_factory=blood_choice)
