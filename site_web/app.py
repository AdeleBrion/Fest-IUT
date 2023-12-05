from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os.path

def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname( __file__ ),p))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../data/BaseDonnee/BD_Festiut.db'))
app.config['SECRET_KEY'] = 'e8ca6d1f-c135-412b-95d0-35768946d93c'

db = SQLAlchemy(app)
