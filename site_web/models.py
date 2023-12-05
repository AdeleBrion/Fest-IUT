from sqlalchemy import CheckConstraint
from .app import db
from flask_login import UserMixin

class Lieu(db.Model):
    __tablename__ = "LIEU"
    idLieu = db.Column(db.Integer, primary_key=True)
    nomLieu = db.Column(db.String(45), nullable=False)
    adresse = db.Column(db.String(45), nullable=False)
    capaciteMax = db.Column(db.Integer, nullable=False)
    photoLieu = db.Column(db.LargeBinary)

class Spectateur(db.Model, UserMixin):
    __tablename__ = "SPECTATEUR"
    idSpectateur = db.Column(db.Integer, primary_key=True)
    nomSpectateur = db.Column(db.String(45), nullable=False)
    prenom = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    motDePasse = db.Column(db.String(45), nullable=False)
    adresse = db.Column(db.String(45), nullable=False)
    infoAnnexes = db.Column(db.String(45))

    def get_id(self):
      return str(self.idSpectateur)

class Billet(db.Model):
    __tablename__ = "BILLET"
    idBillet = db.Column(db.Integer, primary_key=True)
    duree = db.Column(db.Integer, nullable=False)
    prix = db.Column(db.Integer, nullable=False)
    dateValidite = db.Column(db.DateTime, nullable=False)
    idSpectateur = db.Column(db.Integer, db.ForeignKey('SPECTATEUR.idSpectateur'))
    spectateur = db.relationship('Spectateur', backref=db.backref('billets',lazy="dynamic"))

class Style(db.Model):
    __tablename__ = "STYLE"
    idStyle = db.Column(db.Integer, primary_key=True)
    nomStyle = db.Column(db.String(30))

class SousStyle(db.Model):
    __tablename__ = 'SOUSSTYLE'
    idStyle = db.Column(db.Integer, db.ForeignKey('STYLE.idStyle'), primary_key=True)
    style_principale = db.relationship('Style', foreign_keys='SousStyle.idStyle')
    sousStyle = db.Column(db.Integer, db.ForeignKey('STYLE.idStyle'), primary_key=True)
    style_secondaire = db.relationship('Style', foreign_keys='SousStyle.sousStyle')
    

class GroupeMusical(db.Model):
    __tablename__ = "GROUPEMUSICAL"
    idGroupe = db.Column(db.Integer, primary_key=True)
    idStyle = db.Column(db.Integer, db.ForeignKey('STYLE.idStyle'))
    nomGroupe = db.Column(db.String(70), nullable=False)
    descriptionGroupe = db.Column(db.String(70), nullable=False)

    style = db.relationship('Style', backref='groupes')  # Crée une relation avec la classe Style

class Reseaux(db.Model):
    __tablename__ = "RESEAUX"
    idReseau = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.String(100))
    instagram = db.Column(db.String(100))
    tiktok = db.Column(db.String(100))
    
    idGroupe = db.Column(db.Integer, db.ForeignKey('GROUPEMUSICAL.idGroupe'))
    groupe = db.relationship('GroupeMusical', backref='reseaux')

class Concert(db.Model):
    __tablename__ = "CONCERT"
    idConcert = db.Column(db.Integer, primary_key=True)
    idLieu = db.Column(db.Integer, db.ForeignKey('LIEU.idLieu'))
    idGroupe = db.Column(db.Integer, db.ForeignKey('GROUPEMUSICAL.idGroupe'))
    nomConcert = db.Column(db.String(50), nullable=False)
    dateHeureDebut = db.Column(db.DateTime, nullable=False)
    dureeConcert = db.Column(db.Integer, nullable=False)  # en minutes
    dureeMontage = db.Column(db.Integer, nullable=False)  # en minutes
    dureeDemontage = db.Column(db.Integer, nullable=False)  # en minutes
    placesRestantes = db.Column(db.Integer, nullable=False)
    ouvertATous = db.Column(db.Boolean, nullable=False)

    lieu = db.relationship('Lieu', backref='concerts')  # Crée une relation avec la classe Lieu
    groupe_musical = db.relationship('GroupeMusical', backref='concerts')  # Crée une relation avec la classe GroupeMusical

class Inscrire(db.Model):
    __tablename__ = "INSCRIRE"
    idConcert = db.Column(db.Integer, db.ForeignKey('CONCERT.idConcert'), primary_key=True)
    idSpectateur = db.Column(db.Integer, db.ForeignKey('SPECTATEUR.idSpectateur'), primary_key=True)

    concert = db.relationship('Concert', backref='inscriptions')  # Crée une relation avec la classe Concert
    spectateur = db.relationship('Spectateur', backref='inscriptions')  # Crée une relation avec la classe Spectateur


def get_email_spectateur(user):
    return Spectateur.query.filter_by(email=user).first()