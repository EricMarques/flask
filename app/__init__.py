from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

#Controllers -> Models(Tables)
from app.models import tables
from app.login.models import Login
from app.religion.models import Religion
from app.person.models import Person

from app.controllers import default
from app.blueprints.login import login_blueprint
from app.blueprints.blood import blood_blueprint
from app.blueprints.person import person_blueprint
from app.blueprints.religion import religion_blueprint


app.register_blueprint(login_blueprint)
app.register_blueprint(blood_blueprint)
app.register_blueprint(person_blueprint)
app.register_blueprint(religion_blueprint)

#from app.person import models
#from app.person import views