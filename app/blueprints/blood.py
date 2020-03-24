from flask import Blueprint, render_template
from app.models.tables import BloodType
from app.models.forms import BloodTypeForm

blood_blueprint = Blueprint('blood', __name__)

@blood_blueprint.route('/blood', methods=['GET'])
def blood():
    bloodType = BloodTypeForm()
    blood_Type = BloodType.query.filter_by().all()
    
    return render_template('test.html',bloodType=bloodType)