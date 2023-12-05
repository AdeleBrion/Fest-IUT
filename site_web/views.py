from .app import app
from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from .models import get_email_spectateur
from hashlib import sha256

@app.route('/')
def home():
    return render_template('accueil.html')


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