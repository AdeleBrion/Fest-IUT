from datetime import datetime
import json

from .app import app, login_manager, db
from .models import Billet, Inscrire, Jouer, Lieu, Photo, TypeInstrument, Video, get_email_spectateur, Spectateur, GroupeMusical, Concert, Style, TypeBillet, ActiviteAnnexe, Planifier, Appartient, Artiste, Favoriser
from .form import ArtisteForm, ConcertFrom, GroupeFrom, LieuForm
from flask import jsonify, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from hashlib import sha256

@app.route('/')
def home():
    return render_template('accueil.html', concerts=Concert.query.limit(3).all(), title="Accueil Fest-iut")

#-----------------------------------------------------#
#                   Connexion                         #
#-----------------------------------------------------#

class LoginForm(FlaskForm):
    identifiant = StringField('Identifiant')
    mdp = PasswordField('Password')
    def get_authentification_utilisateur(self):
        print(get_email_spectateur("demaret.sullivan@gmail.com"))
        util = get_email_spectateur(self.identifiant.data)
        print(util)
        if util is None:
            return None
        m = sha256()
        m.update(self.mdp.data.encode())
        mdp = m.hexdigest()
        if mdp == util.motDePasse:
            return util
        else:
            return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    f = LoginForm()
    if f.validate_on_submit():
        util = f.get_authentification_utilisateur()
        if util:
            login_user(util)
            return redirect(url_for("home"))
        else:
            return render_template(
                "login.html",
                title = "Page de connexion",
                form=f,
                erreur = "Erreur : Identifiant ou Mot De Passe Incorrect")
    return render_template(
        "login.html",
        title = "Page de connexion",
        form=f)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user):
    return Spectateur.query.get(int(user))

#-----------------------------------------------------#
#                   Compte                            #
#-----------------------------------------------------#

class InscriptionForm(FlaskForm):
    nom = StringField('Nom')
    prenom = StringField('Prenom')
    email = StringField('Email')
    mdp = PasswordField('Password')
    adresse = StringField('Adresse')
    infoAnnexes = StringField('InfoAnnexes')
    def inscription_utilisateur(self):
        spec = Spectateur(
            nomSpectateur=self.nom.data,
            prenom=self.prenom.data,
            email=self.email.data,
            motDePasse=self.mdp.data,
            adresse="",
            infoAnnexes= ""
        )
        return spec


@app.route('/compte')
@login_required
def compte():
    return render_template('compte.html', title ="Mon compte", spectateur = Spectateur.get_current_user_infos())


@app.route('/inscription')
def inscription():
    return render_template('inscription.html', form=InscriptionForm(),title ="Inscription")

@app.route('/billeterie')
@login_required
def billeterie():
    return render_template('billeterie.html', billets = TypeBillet.query.all(), title ="Billeterie")

@app.route('/accueil')
def accueil():
    return render_template('accueil.html')

@app.route("/actualite")
def actualite():
    return render_template('actualite.html', title="L'actu")


#-----------------------------------------------------#
#                   Spectateur                        #
#-----------------------------------------------------#



@app.route('/save/spectateur', methods=("GET", "POST"))
def ajouter_spec():
    f = InscriptionForm()
    spec = Spectateur(
        idSpectateur= Spectateur.getMaxId() + 1,
        nomSpectateur=f.nom.data,
        prenom=f.prenom.data,
        email=f.email.data,
        motDePasse= sha256(f.mdp.data.encode()).hexdigest(),
        adresse= "",
        infoAnnexes=""
    )
    db.session.add(spec)
    db.session.commit()
    return redirect(url_for('login'))


@app.route('/concerts')
def concerts():
    return render_template('concerts.html',styles = Style.query.all())


@app.route('/update_account', methods=['POST'])
def update_account():
    new_nom = request.form['nom']
    new_prenom = request.form['prenom']
    email = request.form['email']
    adresse = request.form['adresse']
    biographie = request.form['biographie']

    spectateur = Spectateur.query.filter_by(nomSpectateur=current_user.nomSpectateur).first()
    if spectateur:
        spectateur.nomSpectateur = new_nom
        spectateur.prenom = new_prenom
        spectateur.email = email
        spectateur.adresse = adresse
        spectateur.infoAnnexes = biographie
        db.session.commit()

    return redirect(url_for('compte'))


@app.route('/concerts/<string:style>')
@login_required
def concerts_style(style):
    style_trouve = Style.query.filter(Style.nomStyle == style).first()
    print(style_trouve)
    return render_template('concerts_style.html', style_trouve= style_trouve ,concerts_likes= Spectateur.recupereConcertFavoris() ,activites = GroupeMusical.query.filter(GroupeMusical.idStyle == style_trouve.idStyle).all(), concerts = Concert.query.join(GroupeMusical).filter(GroupeMusical.idStyle == style_trouve.idStyle).all())

#-----------------------------------------------------#
#                         API                         #
#-----------------------------------------------------#

@app.route('/groupes/liste')
def liste_groupes():
    return jsonify([groupe.serialize() for groupe in GroupeMusical.query.join(Concert).all()])



#-----------------------------------------------------#
#                   INSERTION                         #
#-----------------------------------------------------#


@app.route('/cree/groupe/')
def cree_groupe():
    liste_artiste = Artiste.query.all()
    title = "Créer un groupe"
    f = GroupeFrom()
    f.style.choices = [(style.idStyle, style.nomStyle) for style in Style.query.all()]
    return render_template('form_enregistre_groupe.html', personnes = liste_artiste, title=title, form = f)

@app.route('/cree/groupe/save', methods=['POST'])
def cree_groupe_save():
    f = GroupeFrom()
    nom = f.nomGroupe.data
    description = f.descriptionGroupe.data
    style = f.style.data
    photo = f.photo.data
    video = f.video.data
    liste_personnes_string = f.listePersonnes.data

    try:
        liste_personnes = json.loads(liste_personnes_string)
        print(liste_personnes)
    except json.JSONDecodeError:
        print("Erreur JSON")

    maxidGroupe = GroupeMusical.query.order_by(GroupeMusical.idGroupe.desc()).first().idGroupe
    groupe = GroupeMusical(idGroupe=maxidGroupe+1, nomGroupe=nom, descriptionGroupe=description, idStyle=style)
    db.session.add(groupe)
    
    for artiste in liste_personnes:
        art = Artiste.query.filter(Artiste.nomArtiste == artiste).first()
        print(artiste)
        if art is None:
            idmax = Artiste.query.order_by(Artiste.idArtiste.desc()).first().idArtiste
            art = Artiste(idArtiste=idmax+1, nomArtiste=artiste)
            db.session.add(art)

        appartien = Appartient(idArtiste=art.idArtiste,idGroupe= groupe.idGroupe)
        db.session.add(appartien)

    db.session.commit()
    return redirect(url_for('home'))

@app.route('/supprimer/groupe/<int:id>', methods=['GET'])
def supprimer_groupe_id(id):
    if id is not None:
        groupe = GroupeMusical.query.get(id)
        if groupe:
            idGroupe = groupe.idGroupe
            appartients = Appartient.query.filter(Appartient.idGroupe == idGroupe).all()
            for appartient in appartients:
                db.session.delete(appartient)
            planifier = Planifier.query.filter(Planifier.idGroupe == idGroupe).first()
            if planifier:
                db.session.delete(planifier)
            photo = Photo.query.filter(Photo.idGroupe == idGroupe).first()
            if photo:
                db.session.delete(photo)
            video = Video.query.filter(Video.idGroupe == idGroupe).first()
            if video:
                db.session.delete(video)
            db.session.delete(groupe)
            db.session.commit()
        return redirect(url_for('supprimer_groupe'))
    else:
        groupes = GroupeMusical.query.all()
        return render_template('form_supprimer.html', groupes=groupes)

@app.route('/supprimer/groupe/')
def supprimer_groupe():
    groupes = GroupeMusical.query.all()
    return render_template('form_supprimer.html', groupes=groupes)

@app.route('/cree/concert/')
def cree_concert():
    title = "Créer un concert"
    f = ConcertFrom()
    f.lieu.choices = [(lieu.idLieu, lieu.nomLieu) for lieu in Lieu.query.all()]
    f.groupe.choices = [(groupe.idGroupe, groupe.nomGroupe) for groupe in GroupeMusical.query.all()]
    f.ouvertATous.choices = [(0, "Non"), (1, "Oui")]
    return render_template('form_enregistre_concert.html',form = f, title=title)

@app.route('/cree/concert/save', methods=['POST'])
def cree_concert_save():
    f = ConcertFrom()
    heureDebut = f.heureDebut.data
    dateDebut = f.dateDebut.data
    ouvertATous = f.ouvertATous.data

    ouvertATous = True if ouvertATous == 1 else False
    maxidConcert = Concert.query.order_by(Concert.idConcert.desc()).first().idConcert
    date_et_heure = datetime.combine(dateDebut, heureDebut)    
    concert = Concert(idConcert=maxidConcert+1, idLieu=f.lieu.data, idGroupe=f.groupe.data, nomConcert=f.nomConcert.data, dateHeureDebut= date_et_heure, dureeConcert=f.dureeConcert.data, dureeMontage=f.dureeMontage.data, dureeDemontage=f.dureeDemontage.data, placesRestantes=f.placesRestantes.data, ouvertATous=ouvertATous)
    db.session.add(concert)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/supprimer/concert/<int:id>', methods=['GET'])
def supprimer_concert_id(id):
    if id is not None:
        concert = Concert.query.get(id)
        if concert:
            db.session.delete(concert)
            db.session.commit()
        return redirect(url_for('supprimer_concert'))
    else:
        concerts = Concert.query.all()
        return render_template('form_supprimer.html', concerts=concerts)
    
@app.route('/supprimer/concert/')
def supprimer_concert():
    concerts = Concert.query.all()
    return render_template('form_supprimer.html', concerts=concerts)

@app.route('/cree/artiste/')
def cree_artiste():
    f = ArtisteForm()
    f.instruments.choices = [(instrument.idTypeInstrument, instrument.nomTypeInstrument) for instrument in  TypeInstrument.query.all()]
    return render_template('form_enregistre_artiste.html', form = f, title="ajoute Artiste")

@app.route('/cree/artiste/save', methods=['POST'])
def cree_artiste_save():
    f = ArtisteForm()
    nom = f.nomArtiste.data
    instrument = f.instruments.data
    maxidArtiste = Artiste.query.order_by(Artiste.idArtiste.desc()).first().idArtiste
    artiste = Artiste(idArtiste=maxidArtiste+1, nomArtiste=nom)
    db.session.add(artiste)
    joue = Jouer(idArtiste=maxidArtiste+1, idTypeInstrument=instrument)
    db.session.add(joue)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/supprimer/artiste/<int:id>', methods=['GET'])
def supprimer_artiste_id(id):
    if id is not None:
        artiste = Artiste.query.get(id)
        if artiste:
            idArtiste = artiste.idArtiste
            appartients = Appartient.query.filter(Appartient.idArtiste == idArtiste).all()
            for appartient in appartients:
                db.session.delete(appartient)
            instruments = Jouer.query.filter(Jouer.idArtiste == idArtiste).all()
            for instrument in instruments:
                db.session.delete(instrument)
            db.session.delete(artiste)
            db.session.commit()
        return redirect(url_for('supprimer_artiste'))
    else:
        artistes = Artiste.query.all()
        return render_template('form_supprimer.html', artistes=artistes)
    
@app.route('/supprimer/artiste/')
def supprimer_artiste():
    artistes = Artiste.query.all()
    return render_template('form_supprimer.html', artistes=artistes)

@app.route('/supprimer/utilisateur/<int:id>', methods=['GET'])
def supprimer_utilisateur_id(id):
    if id is not None:
        spectateur = Spectateur.query.get(id)
        if spectateur:
            idSpectateur = spectateur.idSpectateur
            inscriptions = Inscrire.query.filter(Inscrire.idSpectateur == idSpectateur).all()
            for inscription in inscriptions:
                db.session.delete(inscription)
            favoris = Favoriser.query.filter(Favoriser.idSpectateur == idSpectateur).all()
            for favori in favoris:
                db.session.delete(favori)
            billets = Billet.query.filter(Billet.idSpectateur == idSpectateur).all()
            for billet in billets:
                db.session.delete(billet)
            db.session.delete(spectateur)
            db.session.commit()
        return redirect(url_for('supprimer_utilisateur'))
    else:
        utilisateur = Spectateur.query.all()
        return render_template('form_supprimer.html', utilisateurs=utilisateur)
    
@app.route('/supprimer/utilisateur/')
def supprimer_utilisateur():
    utilisateur = Spectateur.query.all()
    return render_template('form_supprimer.html', utilisateurs=utilisateur)

@app.route('/cree/lieu/')
def cree_lieu():
    f = LieuForm()
    return render_template('form_enregistre_lieu.html', form = f, title="ajoute Lieu")

@app.route('/cree/lieu/save', methods=['POST'])
def cree_lieu_save():
    f = LieuForm()
    maxidLieu = Lieu.query.order_by(Lieu.idLieu.desc()).first().idLieu
    lieu = Lieu(idLieu=maxidLieu+1, nomLieu=f.nomLieu.data, adresse=f.adresse.data, capaciteMax=f.capaciteMax.data, photoLieu=None)
    db.session.add(lieu)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/supprimer/lieu/<int:id>', methods=['GET'])
def supprimer_lieu_id(id):
    if id is not None:
        lieu = Lieu.query.get(id)
        if lieu:
            db.session.delete(lieu)
            db.session.commit()
        return redirect(url_for('supprimer_lieu'))
    else:
        utilisateur = Spectateur.query.all()
        return render_template('form_supprimer.html', utilisateurs=utilisateur)
    
@app.route('/supprimer/lieu/')
def supprimer_lieu():
    lieux = Lieu.query.all()
    return render_template('form_supprimer.html', lieux=lieux)

#-----------------------------------------------------#
#                        ADMIN                        #
#-----------------------------------------------------#

@app.route('/panel')
@login_required
def panelAdmin():
    return render_template('panelAdmin.html', title="Panel Admin")

@app.route('/like_concert', methods=['POST'])
def like_concert():
    concert_id = request.form.get('concert_id')
    favori = Favoriser.query.filter_by(idSpectateur=current_user.idSpectateur, idConcert=concert_id).first()
    if favori:
        db.session.delete(favori)
        liked = False
    else:
        favori = Favoriser(idSpectateur=current_user.idSpectateur, idConcert=concert_id)
        db.session.add(favori)
        liked = True
    db.session.commit()
    style = Style.getStyle(GroupeMusical.getGroupe(Concert.getConcert(concert_id).idGroupe).idStyle)
    return concerts_style(style.nomStyle)

@app.route('/moncompte/meeFavoris')
def mes_concerts():
    return render_template('compteFavoris.html', concerts = Spectateur.recupereConcertFavoris())


@app.route('/dislikeFavoris', methods=['POST'])
def dislike_favoris():
    concert_id = request.form.get('concert_id')
    if concert_id is None:
        return "No concert ID provided", 400
    favori = Favoriser.query.filter_by(idSpectateur=current_user.idSpectateur, idConcert=concert_id).first()
    if favori:
        db.session.delete(favori)
        liked = False
    else:
        favori = Favoriser(idSpectateur=current_user.idSpectateur, idConcert=concert_id)
        db.session.add(favori)
        liked = True
    db.session.commit()
    return redirect(url_for('mes_concerts'))
