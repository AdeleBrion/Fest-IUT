from .app import app, login_manager
from .models import get_email_spectateur, Spectateur, GroupeMusical, Concert, Style
from flask import jsonify, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from hashlib import sha256

@app.route('/')
def home():
    return render_template('accueil.html', concerts=Concert.query.limit(3).all())

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

@app.route('/compte')
@login_required
def compte():
    return render_template('compte.html')


@app.route('/inscription')
def inscription():
    return render_template('inscription.html')


@app.route('/billeterie')
@login_required
def billeterie():
    return render_template('billeterie.html')

@app.route('/concerts')
def concerts():
    return render_template('concerts.html',styles = Style.query.all())


@app.route('/concerts/<string:style>')
def concerts_style(style):
    return render_template('concerts_style.html', concerts = Concert.query.join(GroupeMusical).filter(GroupeMusical.idStyle == Style.idStyle).all())

#-----------------------------------------------------#
#                         API                         #
#-----------------------------------------------------#

@app.route('/groupes/liste')
def liste_groupes():
    return jsonify([groupe.serialize() for groupe in GroupeMusical.query.join(Concert).all()])
