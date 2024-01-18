
from flask_wtf import FlaskForm
from wtforms import FileField, HiddenField, SelectField, StringField


class ConcertFrom(FlaskForm):
    nomGroupe = StringField('Nom du groupe')
    descriptionGroupe = StringField('Description du groupe')
    style = SelectField('Style')
    photo = FileField('Photo du groupe')
    video = StringField('Lien de la vidéo')
    listePersonnes = HiddenField('Liste des personnes')