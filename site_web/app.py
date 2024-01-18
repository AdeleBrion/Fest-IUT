from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os.path

def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname( __file__ ),p))

app = Flask(__name__)
username = 'moreira'
password = 'moreira'
host = 'servinfo-maria'
database = 'DBmoreira'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+username+':'+password+'@'+host+'/'+database

app.config['SECRET_KEY'] = 'e8ca6d1f-c135-412b-95d0-35768946d93c'

login_manager = LoginManager(app)
login_manager.login_view = "login"

db = SQLAlchemy(app)
