from flask import Blueprint, render_template, url_for, request, redirect
from app import db
from app.religion.models import Religion
from app.religion.forms import ReligionForm

from datetime import datetime, date

religion_blueprint = Blueprint('religion', __name__)

@religion_blueprint.route('/religion', methods=['GET', 'POST'])
def religionList():
    #religionList = ReligionList()

    religion_list = Religion.query.filter_by().all()
    return render_template('religion/table/religions.html', religion_list = religion_list)#,religionList=religionList)

@religion_blueprint.route('/religionRegister', methods=['GET', 'POST'])
def religion():
    religionForm = ReligionForm()

    if religionForm.validate_on_submit():
        #Religion
        religion = religionForm.religion.data

        #Denomination
        denomination = religionForm.denomination.data
        if denomination == '':
            denomination = None

        #Observations
        observations = religionForm.observations.data
        if observations == '':
            observations = None

        #Action DateTime
        created_at = datetime.now()  #Created at
        updated_at = None  #Updated at  #Deleted(soft delete)
        deleted = 0  #Deleted(soft delete)
        deleted_at = None  #Deleted at(soft delete)

        new_religion = Religion(religion=religion, denomination=denomination, observations=observations, created_at=created_at, updated_at=updated_at, deleted=deleted, deleted_at=deleted_at)

        db.session.add(new_religion)
        db.session.commit()
        # Criar listagem e fazer redirecionamento para ela.
        return redirect(url_for('religion.religionList'))

    else:
        #return personRegistration.errors
        print(religionForm.errors)

    return render_template('religion/form/religionRegister.html', religionForm=religionForm)