from .app import app, login_manager, db
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from .models import get_email_spectateur, Spectateur
from hashlib import sha256

@app.route('/')
def home():
    return render_template('accueil.html')



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
                form=f,
                erreur = "Erreur : Identifiant ou Mot De Passe Incorrect")
    return render_template(
        "login.html",
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
    return render_template('compte.html')


@app.route('/inscription')
def inscription():
    return render_template('inscription.html', form=InscriptionForm())


@app.route('/billeterie')
@login_required
def billeterie():
    return render_template('billeterie.html')




#-----------------------------------------------------#
#                   Spectateur                        #
#-----------------------------------------------------#

@app.route('/save/spectateur', methods=("GET", "POST"))
def ajouter_spec():
    f = InscriptionForm()
    spec = Spectateur(
        nomSpectateur=f.nom.data,
        prenom=f.prenom.data,
        email=f.email.data,
        motDePasse=f.mdp.data,
        adresse=f.adresse.data,
        infoAnnexes=f.infoAnnexes.data
    )
    db.session.add(spec)
    db.session.commit()
    return redirect(url_for('home'))