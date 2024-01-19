from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os.path


app = Flask(__name__)



username = 'brion'
password = 'brion'
host = 'servinfo-maria'
database = 'DBbrion'

# username = 'moreira'
# password = 'moreira'
# host = 'servinfo-maria'
# database = 'DBmoreira'

#username = 'root'
#password = 'root'
#host = 'localhost'
#database = 'sae_festi'


#username = 'susu'
#password = 'susu'
#host = 'localhost'
#database = 'festiut'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+username+':'+password+'@'+host+'/'+database

app.config['SECRET_KEY'] = 'e8ca6d1f-c135-412b-95d0-35768946d93c'

login_manager = LoginManager(app)
login_manager.login_view = "login"

db = SQLAlchemy(app)
