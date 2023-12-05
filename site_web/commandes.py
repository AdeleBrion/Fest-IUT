from .app import app
from hashlib import sha256
import click


@app.cli.command('encode_mdp')
def encode_mdp():
    mdp = input("Entrer le mot de passe à encoder : ")
    m = sha256()
    m.update(mdp.encode())
    print(m.hexdigest())