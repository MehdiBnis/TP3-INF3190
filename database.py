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

import sqlite3


def _build_animal(result_set_item):
    animal = {}
    animal["id"] = result_set_item[0]
    animal["nom"] = result_set_item[1]
    animal["espece"] = result_set_item[2]
    animal["race"] = result_set_item[3]
    animal["age"] = result_set_item[4]
    animal["description"] = result_set_item[5]
    animal["courriel"] = result_set_item[6]
    animal["adresse"] = result_set_item[7]
    animal["ville"] = result_set_item[8]
    animal["cp"] = result_set_item[9]
    return animal


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/animaux.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_animaux(self):
        cursor = self.get_connection().cursor()
        query = ("select id, nom, espece, race, age, description, "
                 "courriel, adresse, ville, cp from animaux")
        cursor.execute(query)
        all_data = cursor.fetchall()
        return [_build_animal(item) for item in all_data]

    def get_animal(self, animal_id):
        cursor = self.get_connection().cursor()
        query = ("select id, nom, espece, race, age, description, courriel, "
                 "adresse, ville, cp from animaux where id = ?")
        cursor.execute(query, (animal_id,))
        item = cursor.fetchone()
        if item is None:
            return item
        else:
            return _build_animal(item)

    def add_animal(self, nom, espece, race, age, description, courriel,
                   adresse, ville, cp):
        connection = self.get_connection()
        query = ("insert into animaux(nom, espece, race, age, description, "
                 "courriel, adresse, ville, cp) "
                 "values(?, ?, ?, ?, ?, ?, ?, ?, ?)")
        connection.execute(query, (nom, espece, race, age, description,
                                   courriel, adresse, ville, cp))
        cursor = connection.cursor()
        cursor.execute("select last_insert_rowid()")
        lastId = cursor.fetchone()[0]
        connection.commit()
        return lastId

    def search_animaux(self, search_term):
        connection = self.get_connection()
        query = ("SELECT id, nom, espece, race, age, description, courriel, adresse, ville, cp "
                 "FROM animaux "
                 "WHERE nom LIKE ? OR espece LIKE ? OR description LIKE ?")
        search_term = f'%{search_term}%'
        cursor = connection.execute(query, (search_term, search_term, search_term))
        results = cursor.fetchall()
        return [_build_animal(item) for item in results]
    
    def get_random_animaux(self, limit=5):
        cursor = self.get_connection().cursor()
        query = """
        SELECT id, nom, espece, race, age, description, courriel, adresse, ville, cp 
        FROM animaux 
        ORDER BY RANDOM() 
        LIMIT ?
        """
        cursor.execute(query, (limit,))
        return [_build_animal(item) for item in cursor.fetchall()]
    
    def get_newest_animaux(self, limit=6):
        cursor = self.get_connection().cursor()
        query = """
        SELECT id, nom, espece, race, age, description, courriel, adresse, ville, cp 
        FROM animaux 
        ORDER BY id DESC 
        LIMIT ?
        """
        cursor.execute(query, (limit,))
        return [_build_animal(item) for item in cursor.fetchall()]
