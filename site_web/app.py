from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

username = 'root'
password = 'root'
host = 'localhost'
database = 'sae_festi'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+username+':'+password+'@'+host+'/'+database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
