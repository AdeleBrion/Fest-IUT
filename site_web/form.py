
from flask_wtf import FlaskForm
from wtforms import FileField, HiddenField, SelectField, StringField, TimeField, IntegerField, DateField
from wtforms.validators import DataRequired

class GroupeFrom(FlaskForm):
    nomGroupe = StringField('Nom du groupe')
    descriptionGroupe = StringField('Description du groupe')
    style = SelectField('Style')
    photo = FileField('Photo du groupe')
    video = StringField('Lien de la vidéo')
    listePersonnes = HiddenField('Liste des personnes')

class ConcertFrom(FlaskForm):
    lieu = SelectField('Lieu')
    groupe = SelectField('Groupe')
    nomConcert = StringField('Nom du concert', validators=[DataRequired()])
    heureDebut = TimeField('heure de début', validators=[DataRequired()])
    dateDebut = DateField('Date de début', validators=[DataRequired()])
    dureeConcert = IntegerField('Durée du concert', validators=[DataRequired()])
    dureeMontage = IntegerField('Durée du montage', validators=[DataRequired()])
    dureeDemontage = IntegerField('Durée du démontage', validators=[DataRequired()])
    placesRestantes = IntegerField('Nombre de places disponibles', validators=[DataRequired()])
    ouvertATous = SelectField('Ouvert à tous')

class ArtisteForm(FlaskForm):
    nomArtiste = StringField('Nom de l\'artiste', validators=[DataRequired()])
    instruments = SelectField('Instrument')

class LieuForm(FlaskForm):
    nomLieu = StringField('Nom du Lieu', validators=[DataRequired()])
    adresse = StringField('L\'adresse du lieu', validators=[DataRequired()])
    capaciteMax = IntegerField('La capacité max du lieu',validators=[DataRequired()])
    photolieu = FileField('Une photo du lieu')

class StyleForm(FlaskForm):
    nomStyle = StringField('Nom du Style', validators=[DataRequired()])
    imageStyle = FileField('Image du Style')
