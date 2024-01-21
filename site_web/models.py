from sqlalchemy import CheckConstraint
from .app import db
from flask_login import UserMixin, current_user

class Lieu(db.Model):
    __tablename__ = "LIEU"
    idLieu = db.Column(db.Integer, primary_key=True)
    nomLieu = db.Column(db.String(45), nullable=False)
    adresse = db.Column(db.String(45), nullable=False)
    capaciteMax = db.Column(db.Integer, nullable=False)
    photoLieu = db.Column(db.LargeBinary)

class Role(db.Model):
    __tablename__ = "ROLE"
    idRole = db.Column(db.Integer, primary_key=True)
    nomRole = db.Column(db.String(30), nullable=False)

class Spectateur(db.Model, UserMixin):
    __tablename__ = "SPECTATEUR"
    idSpectateur = db.Column(db.Integer, primary_key=True)
    nomSpectateur = db.Column(db.String(45), nullable=False)
    prenom = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    motDePasse = db.Column(db.String(45), nullable=False)
    adresse = db.Column(db.String(45), nullable=False)
    infoAnnexes = db.Column(db.String(45))
    idRole = db.Column(db.Integer, db.ForeignKey('ROLE.idRole'), nullable=False)
    role = db.relationship('Role', backref=db.backref('rols',lazy="dynamic"))

    def get_id(self):
      return str(self.idSpectateur)
    
    def getMaxId():
        return Spectateur.query.order_by(Spectateur.idSpectateur.desc()).first().idSpectateur
    
    def is_admin(self):
        return True if self.idRole == Role.query.filter_by(nomRole="Administrateur").first().idRole else False
    
    def get_current_user_infos():
        return Spectateur.query.filter_by(idSpectateur=current_user.idSpectateur).first()
    def recupereConcertFavoris():
        favoris = Favoriser.query.filter_by(idSpectateur=current_user.idSpectateur).all()
        listeConcerts = []
        for favori in favoris:
            listeConcerts.append(Concert.query.filter_by(idConcert=favori.idConcert).first())
        return listeConcerts

class TypeBillet(db.Model):
    __tablename__ = "TYPEBILLET"
    idTypeBillet = db.Column(db.Integer, primary_key=True)
    intitule = db.Column(db.String(50))
    description = db.Column(db.String(5000))
    prix = db.Column(db.Integer, nullable=False)
    duree = db.Column(db.Integer, nullable=False)

class Billet(db.Model):
    __tablename__ = "BILLET"
    idBillet = db.Column(db.Integer, primary_key=True)
    idTypeBillet = db.Column(db.Integer, db.ForeignKey('TYPEBILLET.idTypeBillet'))
    typeBillet = db.relationship('TypeBillet', backref=db.backref('billets',lazy="dynamic"))
    dateDebut = db.Column(db.DateTime, nullable=False)
    idSpectateur = db.Column(db.Integer, db.ForeignKey('SPECTATEUR.idSpectateur'))
    spectateur = db.relationship('Spectateur', backref=db.backref('billets',lazy="dynamic"))

class Style(db.Model):
    __tablename__ = "STYLE"
    idStyle = db.Column(db.Integer, primary_key=True)
    nomStyle = db.Column(db.String(30))
    imageStyle = db.Column(db.String(100))

    def getNomToUpperCase(self):
        return self.nomStyle.upper()

    def getImage(self):
        return self.imageStyle if self.imageStyle else "confetti.jpg"
    def getStyle(idStyle):
        return Style.query.filter_by(idStyle=idStyle).first()

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

    def serialize(self):
        unConcert = Concert.query.filter_by(idGroupe=self.idGroupe).first()
        return {
            "idGroupe": self.idGroupe,
            "idStyle": self.idStyle,
            "nomGroupe": self.nomGroupe,
            "descriptionGroupe": self.descriptionGroupe,
            "style": self.style.nomStyle,
            "concert": unConcert.serialize() if unConcert else None,
            "photos": self.photos,
        }
    def getGroupe(idGroupe):
        return GroupeMusical.query.filter_by(idGroupe=idGroupe).first()
    def get_membres(self):
        return Appartient.query.filter_by(idGroupe=self.idGroupe).all()
    def get_instruments(self):
        membres = Appartient.query.filter_by(idGroupe=self.idGroupe).all()
        instruments = set()  # Utiliser un ensemble pour éviter les doublons
        for membre in membres:
            artiste = membre.artiste
            instruments_membre = Jouer.query.filter_by(idArtiste=artiste.idArtiste).all()
            for instrument in instruments_membre:
                instruments.add(instrument.type_instrument.nomTypeInstrument)
        return list(instruments)
        
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

    def serialize(self):
        return {
        "idConcert": self.idConcert,
        "idLieu": self.idLieu,
        "idGroupe": self.idGroupe,
        "nomConcert": self.nomConcert,
        "dateHeureDebut": self.dateHeureDebut,
        "dureeConcert": self.dureeConcert,
        "dureeMontage": self.dureeMontage,
        "dureeDemontage": self.dureeDemontage,
        "placesRestantes": self.placesRestantes,
        "ouvertATous": self.ouvertATous,
        "lieu": self.lieu.nomLieu,
        # "groupe_musical": self.groupe_musical.nomGroupe,
        # "inscriptions": self.inscriptions,
        # "favorises": self.favorises,
        }
    def getConcert(idConcert):
        return Concert.query.filter_by(idConcert=idConcert).first()

class Inscrire(db.Model):
    __tablename__ = "INSCRIRE"
    idConcert = db.Column(db.Integer, db.ForeignKey('CONCERT.idConcert'), primary_key=True)
    idSpectateur = db.Column(db.Integer, db.ForeignKey('SPECTATEUR.idSpectateur'), primary_key=True)

    concert = db.relationship('Concert', backref='inscriptions')  # Crée une relation avec la classe Concert
    spectateur = db.relationship('Spectateur', backref='inscriptions')  # Crée une relation avec la classe Spectateur

class Favoriser(db.Model):
    __tablename__ = "FAVORISER"
    idConcert = db.Column(db.Integer, db.ForeignKey('CONCERT.idConcert'), primary_key=True)
    idSpectateur = db.Column(db.Integer, db.ForeignKey('SPECTATEUR.idSpectateur'), primary_key=True)

    concert = db.relationship('Concert', backref='favorises')  # Crée une relation avec la classe Concert
    spectateur = db.relationship('Spectateur', backref='favorises')  # Crée une relation avec la classe Spectateur

class Hebergement(db.Model):
    __tablename__ = "HEBERGEMENT"
    idHebergement = db.Column(db.Integer, primary_key=True, nullable=False)
    nomHebergement = db.Column(db.String(30), nullable=False)
    nbMax = db.Column(db.Integer, nullable=False)

class Accueilir(db.Model):
    __tablename__ = "ACCUEILIR"
    idGroupe = db.Column(db.Integer, db.ForeignKey('GROUPEMUSICAL.idGroupe'), primary_key=True)
    idHebergement = db.Column(db.Integer, db.ForeignKey('HEBERGEMENT.idHebergement'), primary_key=True)
    dateHeureHeb = db.Column(db.DateTime, nullable=False)  # Utilisez le type DateTime pour stocker la date et l'heure
    nbPersonne = db.Column(db.Integer, nullable=False)

    groupe_musical = db.relationship('GroupeMusical', backref='hebergements')  # Crée une relation avec la classe GroupeMusical
    hebergement = db.relationship('Hebergement', backref='groupes_accueillis')  # Crée une relation avec la classe Hebergement

class ActiviteAnnexe(db.Model):
    __tablename__ = "ACTIVITEANNEXE"
    idActivite = db.Column(db.Integer, primary_key=True)
    descriptionActivite = db.Column(db.String(80), nullable=False)
    dateheureActivite = db.Column(db.DateTime)
    accessibleAuPublic = db.Column(db.Boolean, nullable=False)

class Planifier(db.Model):
    __tablename__ = "PLANIFIER"
    idGroupe = db.Column(db.Integer, db.ForeignKey('GROUPEMUSICAL.idGroupe'), primary_key=True)
    idActivite = db.Column(db.Integer, db.ForeignKey('ACTIVITEANNEXE.idActivite'), primary_key=True)
    dureePlanification = db.Column(db.Integer, nullable=False)

    groupe_musical = db.relationship('GroupeMusical', backref='activites_planifiees')  # Crée une relation avec la classe GroupeMusical
    activite_annexe = db.relationship('ActiviteAnnexe', backref='groupes_planifies')  # Crée une relation avec la classe ActiviteAnnexe

class TypeInstrument(db.Model):
    __tablename__ = "TYPEINSTRUMENT"
    idTypeInstrument = db.Column(db.Integer, primary_key=True)
    nomTypeInstrument = db.Column(db.String(30), nullable=False)

class Artiste(db.Model):
    __tablename__ = "ARTISTE"
    idArtiste = db.Column(db.Integer, primary_key=True)
    nomArtiste = db.Column(db.String(30), nullable=False)

class Jouer(db.Model):
    __tablename__ = "JOUER"
    idTypeInstrument = db.Column(db.Integer, db.ForeignKey('TYPEINSTRUMENT.idTypeInstrument'), primary_key=True)
    idArtiste = db.Column(db.Integer, db.ForeignKey('ARTISTE.idArtiste'), primary_key=True)

    type_instrument = db.relationship('TypeInstrument',backref=db.backref("artistes_jouant", lazy="dynamic"))
    artiste = db.relationship('Artiste', backref=db.backref("instruments_joues", lazy="dynamic"))

class Appartient(db.Model):
    __tablename__ = "APPARTIENT"
    idGroupe = db.Column(db.Integer, db.ForeignKey('GROUPEMUSICAL.idGroupe'), primary_key=True)
    idArtiste = db.Column(db.Integer, db.ForeignKey('ARTISTE.idArtiste'), primary_key=True)

    groupe_musical = db.relationship('GroupeMusical', backref='artistes_membres')  # Crée une relation avec la classe GroupeMusical
    artiste = db.relationship('Artiste', backref='groupes_appartenant')  # Crée une relation avec la classe Artiste

class Photo(db.Model):
    __tablename__ = "PHOTO"
    idPhoto = db.Column(db.Integer, primary_key=True)
    idGroupe = db.Column(db.Integer, db.ForeignKey('GROUPEMUSICAL.idGroupe'), nullable=False)
    filePathPhoto = db.Column(db.LargeBinary)

    groupe_musical = db.relationship('GroupeMusical', backref='photos')  # Crée une relation avec la classe GroupeMusical

    def serialize(self):
        return {
            "idPhoto": self.idPhoto,
            "idGroupe": self.idGroupe,
            "filePathPhoto": self.filePathPhoto,
        }

class Video(db.Model):
    __tablename__ = "VIDEO"
    idVideo = db.Column(db.Integer, primary_key=True)
    idGroupe = db.Column(db.Integer, db.ForeignKey('GROUPEMUSICAL.idGroupe'), nullable=False)
    filePathVideo = db.Column(db.String(50), nullable=False)

    groupe_musical = db.relationship('GroupeMusical', backref='videos')  # Crée une relation avec la classe GroupeMusical


def get_email_spectateur(user):
    return Spectateur.query.filter_by(email=user).first()