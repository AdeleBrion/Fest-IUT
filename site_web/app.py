from flask import Flask

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../data/BaseDonnee/DB_Festiut.db'))
app.config['SECRET_KEY'] = 'e8ca6d1f-c135-412b-95d0-35768946d93c'