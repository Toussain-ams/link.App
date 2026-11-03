"""
Application web de partage de liens.
Technologies : Python, Flask, SQLite, HTML, CSS et JavaScript.
"""

import re
import sqlite3
from pathlib import Path
from urllib.parse import urlparse

from flask import Flask, flash, jsonify, redirect, render_template, request, url_for

# Chemin absolu vers le dossier du projet et la base de données SQLite.
BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "liens.db"

app = Flask(__name__)
app.secret_key = "cle-de-developpement-a-remplacer"


def get_db_connection():
    """Ouvre une connexion SQLite et permet d'accéder aux colonnes par leur nom."""
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Crée la table des liens si elle n'existe pas encore."""
    with get_db_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS liens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                titre TEXT NOT NULL,
                categorie TEXT NOT NULL,
                date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()


def url_est_valide(url):
    """Vérifie que l'adresse possède http/https et un nom de domaine plausible."""
    try:
        parsed = urlparse(url.strip())
        return (
            parsed.scheme in ("http", "https")
            and bool(parsed.netloc)
            and "." in parsed.netloc
            and not re.search(r"\s", url)
        )
    except ValueError:
        return False

@app.route("/")
def accueil():
    """Affiche la page d'accueil."""
    return render_template("index.html")


@app.route("/liens")
def afficher_liens():
    """Affiche tous les liens enregistrés."""
    with get_db_connection() as connection:
        liens = connection.execute(
            "SELECT * FROM liens ORDER BY date_ajout DESC, id DESC"
        ).fetchall()

    return render_template("liens.html", liens=liens)
@app.route("/aleatoire")

def lien_aleatoire():
    """Sélectionne un lien au hasard et le renvoie au navigateur au format JSON."""
    with get_db_connection() as connection:
        lien = connection.execute(
            "SELECT id, url, titre, categorie FROM liens ORDER BY RANDOM() LIMIT 1"
        ).fetchone()

    if lien is None:
        return jsonify({"message": "Aucun lien enregistré pour le moment."}), 404

    return jsonify(dict(lien))


@app.route("/ajouter", methods=["POST"])
def ajouter_lien():
    """Récupère les champs du formulaire, les valide et enregistre le lien."""
    url = request.form.get("url", "").strip()
    titre = request.form.get("titre", "").strip()
    categorie = request.form.get("categorie", "").strip()

    if not url or not titre or not categorie:
        flash("Tous les champs sont obligatoires.", "erreur")
    elif not url_est_valide(url):
        flash("L'adresse URL n'est pas valide. Exemple : https://example.com", "erreur")
    else:
        # La requête paramétrée évite de placer directement les valeurs dans le SQL.
        with get_db_connection() as connection:
            connection.execute(
                "INSERT INTO liens (url, titre, categorie) VALUES (?, ?, ?)",
                (url, titre, categorie)
            )
            connection.commit()
        flash("Lien ajouté avec succès !", "succes")

    return redirect(url_for("accueil"))



if __name__ == "__main__":
    # Prépare la base de données avant le démarrage du serveur Flask.
    init_db()
    app.run(debug = True)
