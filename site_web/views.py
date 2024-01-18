import json

from .app import app, login_manager, db
from .models import get_email_spectateur, Spectateur, GroupeMusical, Concert, Style, TypeBillet, ActiviteAnnexe, Planifier, Appartient, Artiste
from .form import ConcertFrom
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
    return redirect(url_for('home'))
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
def concerts_style(style):
    style_trouve = Style.query.filter(Style.nomStyle == style).first()
    return render_template('concerts_style.html', activites = GroupeMusical.query.filter(GroupeMusical.idStyle == style_trouve.idStyle).all(), concerts = Concert.query.join(GroupeMusical).filter(GroupeMusical.idStyle == style_trouve.idStyle).all())

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
    f = ConcertFrom()
    f.style.choices = [(style.idStyle, style.nomStyle) for style in Style.query.all()]
    return render_template('form_enregistre_groupe.html', personnes = liste_artiste, title=title, form = f)

@app.route('/cree/groupe/save', methods=['POST'])
def cree_groupe_save():
    f = ConcertFrom()
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
            db.session.delete(groupe)
            db.session.commit()
        return redirect(url_for('supprimer_groupe'))
    else:
        groupes = GroupeMusical.query.all()
        return render_template('form_supprimer_groupe.html', groupes=groupes)

@app.route('/supprimer/groupe/')
def supprimer_groupe():
    groupes = GroupeMusical.query.all()
    return render_template('form_supprimer_groupe.html', groupes=groupes)

@app.route('/cree/concert/')
def cree_concert():
    title = "Créer un concert"
    liste_groupes = GroupeMusical.query.all()
    return render_template('form_enregistre_concert.html', groupes = liste_groupes, title=title)

#-----------------------------------------------------#
#                        ADMIN                        #
#-----------------------------------------------------#

@app.route('/panel')
@login_required
def panelAdmin():
    return render_template('panelAdmin.html', title="Panel Admin")
