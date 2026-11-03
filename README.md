# LinkApp — Application de partage de liens

Petit projet pédagogique réalisé avec Python / Flask, SQLite, HTML, CSS et JavaScript.

1. Fonctionnalités réalisées

- Ajouter un lien avec son titre, son URL et sa catégorie.
- Vérifier que l'URL utilise `http://` ou `https://` et possède un domaine.
- Enregistrer les liens dans une base SQLite (`liens.db`).
- Afficher les liens du plus récent au plus ancien.
- Choisir et afficher un lien au hasard sans recharger la page.

2. Préparation dans VS Code

Ouvrir le dossier `partage_liens` dans VS Code, puis ouvrir le terminal intégré.

Créer un environnement virtuel (recommandé) :

python -m venv venv


Sur Windows :


venv\Scripts\activate


Installer Flask 
`
python -m pip install -r requirements.txt

 3. Lancer le projet

Dans le terminal :


python app.py


Ouvrir ensuite l'adresse affichée dans le terminal,  :

`http://127.0.0.1:5000`

La base `liens.db` et sa table sont créées automatiquement au premier démarrage.
 4. Comprendre les fichiers

- `app.py` : routes web, validation, connexion SQLite et logique Python.
- `templates/index.html` : structure de la page et formulaire.
- `static/css/style.css` : apparence, couleurs et adaptation mobile.
- `static/js/main.js` : clic sur le bouton aléatoire et appel asynchrone à Flask.
- `requirements.txt` : dépendances Python.
- `liens.db` : base de données créée au lancement.

5. Quelques notions à retenir

- Une route Flask associe une URL à une fonction Python.
- `request.form` récupère les champs envoyés par le formulaire.
- `sqlite3` permet de stocker les données localement.
- `fetch()` permet à JavaScript de demander des données au serveur.
- `ORDER BY date_ajout DESC` trie les liens du plus récent au plus ancien.

6. Git (facultatif pour commencer)


git init
git add .
git commit -m "Initialisation du projet LinkShare"
git add .
git commit -m "Ajout du formulaire et de la liste des liens"
git add .
git commit -m "Ajout du lien aleatoire et validation URL"

