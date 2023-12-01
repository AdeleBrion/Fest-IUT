from .app import app, db
from .models import Lieu, Spectateur, Concert, Style, SousStyle, Billet, GroupeMusical
from flask import render_template


@app.route('/')
def home():
    concert = Concert.query.all()
    return render_template('home.html', Concerts = concert)

@app.route('/index/')
def index():
    return render_template('index.html')
