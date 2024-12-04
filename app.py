# Copyright 2024 Mehdi Bennis (BENM80120206) / Kanykey Albanova (ALBK02529305)
# UQAM - Génie informatique et logiciel
# TP3 - INF3190
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import url_for
from .database import Database
from .entree import valider_formulaire

app = Flask(__name__, static_url_path="", static_folder="static")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.route('/')
def accueil():
    random_animaux = get_db().get_random_animaux(limit=6)  # Récupérer cinq animaux aléatoires
    return render_template('index.html', newest_animaux=random_animaux)


@app.route('/formulaire', methods=['GET', 'POST'])
def form():
    # GET
    if request.method == 'GET':
        return render_template('form.html'), 200
    # POST
    elif request.method == 'POST':
        # Récupérer les données
        nom = request.form['nom']
        espece = request.form['espece']
        race = request.form['race']
        age = request.form['age']
        description = request.form['description']
        courriel = request.form['courriel']
        adresse = request.form['adresse']
        ville = request.form['ville']
        cp = request.form['cp']

        # Valider le formulaire
        if valider_formulaire(nom, espece, race, age, description, courriel, adresse, ville, cp):
            animal_id = get_db().add_animal(nom, espece, race, age, description, courriel, adresse, ville, cp)
            return redirect(url_for('info_animal', animal_id=animal_id)), 301
        else:
            return render_template('form.html'), 200


@app.route('/animal/<int:animal_id>')
def info_animal(animal_id):
    # Récupérer les informations de l'animal
    animal = get_db().get_animal(animal_id)
    return render_template('animal.html', animal=animal), 200


@app.errorhandler(404)
def page_introuvable(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/recherche', methods=['GET'])
def recherche():
    search_term = request.args.get('q', '')
    animaux = get_db().search_animaux(search_term)
    return render_template('search_results.html', animaux=animaux)
