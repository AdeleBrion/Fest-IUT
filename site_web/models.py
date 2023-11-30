from sqlalchemy import CheckConstraint
from .app import db

class Lieu(db.Model):
    __tablename__ = "lieu"
    idLieu = db.Column(db.Integer, primary_key=True)
    nomLieu = db.Column(db.String(45), nullable=False)
    adresse = db.Column(db.String(45), nullable=False)
    capaciteMax = db.Column(db.Integer, nullable=False)
    photoLieu = db.Column(db.LargeBinary)

class Spectateur(db.Model):
    __tablename__ = "spectateur"
    idSpectateur = db.Column(db.Integer, primary_key=True)
    nomSpectateur = db.Column(db.String(45), nullable=False)
    prenom = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    motDePasse = db.Column(db.String(45), nullable=False)
    adresse = db.Column(db.String(45), nullable=False)
    infoAnnexes = db.Column(db.String(45))

class Billet(db.Model):
    __tablename__ = "billet"
    idBillet = db.Column(db.Integer, primary_key=True)
    duree = db.Column(db.Integer, nullable=False)
    prix = db.Column(db.Integer, nullable=False)
    dateValidite = db.Column(db.DateTime, nullable=False)
    idSpectateur = db.Column(db.Integer, db.ForeignKey('spectateur.idSpectateur'))
    spectateur = db.relationship('Spectateur', backref=db.backref('billets',lazy="dynamic"))

class Style(db.Model):
    __tablename__ = "style"
    idStyle = db.Column(db.Integer, primary_key=True)
    nomStyle = db.Column(db.String(30))

class SousStyle(db.Model):
    __tablename__ = 'sousstyle'
    idStyle = db.Column(db.Integer, db.ForeignKey('style.idStyle'), primary_key=True)
    style_principale = db.relationship('Style', foreign_keys='SousStyle.idStyle')
    sousStyle = db.Column(db.Integer, db.ForeignKey('style.idStyle'), primary_key=True)
    style_secondaire = db.relationship('Style', foreign_keys='SousStyle.sousStyle')
    

class GroupeMusical(db.Model):
    __tablename__ = "groupemusical"
    idGroupe = db.Column(db.Integer, primary_key=True)
    idStyle = db.Column(db.Integer, db.ForeignKey('style.idStyle'))
    nomGroupe = db.Column(db.String(70), nullable=False)
    descriptionGroupe = db.Column(db.String(70), nullable=False)

    style = db.relationship('Style', backref='groupes')  # Crée une relation avec la classe Style

class Reseaux(db.Model):
    __tablename__ = "reseaux"
    idReseau = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.String(100))
    instagram = db.Column(db.String(100))
    tiktok = db.Column(db.String(100))
    
    idGroupe = db.Column(db.Integer, db.ForeignKey('groupemusical.idGroupe'))
    groupe = db.relationship('GroupeMusical', backref='reseaux')

class Concert(db.Model):
    __tablename__ = "concert"
    idConcert = db.Column(db.Integer, primary_key=True)
    idLieu = db.Column(db.Integer, db.ForeignKey('lieu.idLieu'))
    idGroupe = db.Column(db.Integer, db.ForeignKey('groupemusical.idGroupe'))
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
    __tablename__ = "inscrire"
    idConcert = db.Column(db.Integer, db.ForeignKey('concert.idConcert'), primary_key=True)
    idSpectateur = db.Column(db.Integer, db.ForeignKey('spectateur.idSpectateur'), primary_key=True)

    concert = db.relationship('Concert', backref='inscriptions')  # Crée une relation avec la classe Concert
    spectateur = db.relationship('Spectateur', backref='inscriptions')  # Crée une relation avec la classe Spectateur

class Favoriser(db.Model):
    __tablename__ = "favoriser"
    idConcert = db.Column(db.Integer, db.ForeignKey('concert.idConcert'), primary_key=True)
    idSpectateur = db.Column(db.Integer, db.ForeignKey('spectateur.idSpectateur'), primary_key=True)

    concert = db.relationship('Concert', backref='favorises')  # Crée une relation avec la classe Concert
    spectateur = db.relationship('Spectateur', backref='favorises')  # Crée une relation avec la classe Spectateur

class Hebergement(db.Model):
    __tablename__ = "hebergement"
    idHebergement = db.Column(db.Integer, primary_key=True, nullable=False)
    nomHebergement = db.Column(db.String(30), nullable=False)
    nbMax = db.Column(db.Integer, nullable=False)

class Accueillir(db.Model):
    __tablename__ = "accueillir"
    idGroupe = db.Column(db.Integer, db.ForeignKey('groupemusical.idGroupe'), primary_key=True)
    idHebergement = db.Column(db.Integer, db.ForeignKey('hebergement.idHebergement'), primary_key=True)
    dateHeureHeb = db.Column(db.DateTime, nullable=False)  # Utilisez le type DateTime pour stocker la date et l'heure
    nbPersonne = db.Column(db.Integer, nullable=False)

    groupe_musical = db.relationship('GroupeMusical', backref='hebergements')  # Crée une relation avec la classe GroupeMusical
    hebergement = db.relationship('Hebergement', backref='groupes_accueillis')  # Crée une relation avec la classe Hebergement

class ActiviteAnnexe(db.Model):
    __tablename__ = "activiteannexe"
    idActivite = db.Column(db.Integer, primary_key=True)
    descriptionActivite = db.Column(db.String(80), nullable=False)
    dateheureActivite = db.Column(db.DateTime)
    accessibleAuPublic = db.Column(db.Boolean, nullable=False)

class Planifier(db.Model):
    __tablename__ = "planifier"
    idGroupe = db.Column(db.Integer, db.ForeignKey('groupemusical.idGroupe'), primary_key=True)
    idActivite = db.Column(db.Integer, db.ForeignKey('activiteannexe.idActivite'), primary_key=True)
    dureePlanification = db.Column(db.Integer, nullable=False)

    groupe_musical = db.relationship('GroupeMusical', backref='activites_planifiees')  # Crée une relation avec la classe GroupeMusical
    activite_annexe = db.relationship('ActiviteAnnexe', backref='groupes_planifies')  # Crée une relation avec la classe ActiviteAnnexe

class TypeInstrument(db.Model):
    __tablename__ = "typeinstrument"
    idTypeInstrument = db.Column(db.Integer, primary_key=True)
    nomTypeInstrument = db.Column(db.String(30), nullable=False)

class Artiste(db.Model):
    __tablename__ = "artiste"
    idArtiste = db.Column(db.Integer, primary_key=True)
    nomArtiste = db.Column(db.String(30), nullable=False)

class Jouer(db.Model):
    __tablename__ = "jouer"
    idTypeInstrument = db.Column(db.Integer, db.ForeignKey('typeinstrument.idTypeInstrument'), primary_key=True)
    idArtiste = db.Column(db.Integer, db.ForeignKey('artiste.idArtiste'), primary_key=True)

    type_instrument = db.relationship('TypeInstrument',backref=db.backref("artistes_jouant", lazy="dynamic"))
    artiste = db.relationship('Artiste', backref=db.backref("instruments_joues", lazy="dynamic"))

class Appartient(db.Model):
    __tablename__ = "appartient"
    idGroupe = db.Column(db.Integer, db.ForeignKey('groupemusical.idGroupe'), primary_key=True)
    idArtiste = db.Column(db.Integer, db.ForeignKey('artiste.idArtiste'), primary_key=True)

    groupe_musical = db.relationship('GroupeMusical', backref='artistes_membres')  # Crée une relation avec la classe GroupeMusical
    artiste = db.relationship('Artiste', backref='groupes_appartenant')  # Crée une relation avec la classe Artiste

class Photo(db.Model):
    __tablename__ = "photo"
    idPhoto = db.Column(db.Integer, primary_key=True)
    idGroupe = db.Column(db.Integer, db.ForeignKey('groupemusical.idGroupe'), nullable=False)
    filePathPhoto = db.Column(db.LargeBinary)

    groupe_musical = db.relationship('GroupeMusical', backref='photos')  # Crée une relation avec la classe GroupeMusical

class Video(db.Model):
    __tablename__ = "video"
    idVideo = db.Column(db.Integer, primary_key=True)
    idGroupe = db.Column(db.Integer, db.ForeignKey('groupemusical.idGroupe'), nullable=False)
    filePathVideo = db.Column(db.String(50), nullable=False)

    groupe_musical = db.relationship('GroupeMusical', backref='videos')  # Crée une relation avec la classe GroupeMusical
