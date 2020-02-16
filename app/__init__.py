from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
#mysql://nomeUsuario:senhaUsuario@servidor/nomeBancoDados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://eric:Erc_m1234@localhost/aulaFlask'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default
