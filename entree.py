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

# Importer la vérification du regex
import re


def valider_nom(nom):
    if (
        nom is None
        or nom == ""
        or not (3 <= len(nom) <= 20)
        or (',' in nom)
    ):
        return False
    return True


def valider_espece(espece):
    if (
        espece is None
        or espece == ""
        or (',' in espece)
        or (len(espece) > 25)
    ):
        return False
    return True


def valider_race(race):
    if (
        race is None
        or race == ""
        or (',' in race)
        or (len(race) > 25)
    ):
        return False
    return True


def valider_age(age):
    if (
        age is None
        or age == ""
        or not (0 <= int(age) <= 30)
        or (',' in age)
    ):
        return False
    return True


def valider_description(description):
    if (
        description is None
        or description == ""
        or (',' in description)
        or len(description) > 500
    ):
        return False
    return True


def valider_courriel(courriel):
    format_courriel = (r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:['
                       r'\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:['
                       r'a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4]['
                       r'0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:['
                       r'\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])')
    if (
        courriel is None
        or courriel == ""
        or not re.match(format_courriel, courriel)
        or (',' in courriel)
        or (len(courriel) > 80)
    ):
        return False
    return True


def valider_adresse(adresse):
    format_adresse = r'^\d+\s[0-9A-Za-z\s]+$'
    if (
        adresse is None
        or adresse == ""
        or not re.match(format_adresse, adresse)
        or (',' in adresse)
        or (len(adresse) > 75)
    ):
        return False
    return True


def valider_ville(ville):
    if (
        ville is None
        or ville == ""
        or (',' in ville)
        or (len(ville) > 75)
    ):
        return False
    return True


def valider_code_postal(cp):
    format_cp = r'^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$'
    if (
        cp is None
        or cp == ""
        or not re.match(format_cp, cp)
        or (',' in cp)
        or (len(cp) > 7)
    ):
        return False
    return True


def valider_formulaire(nom, espece, race, age, description, courriel, adresse, ville, code_postal):
    if (
        valider_nom(nom) and
        valider_espece(espece) and
        valider_race(race) and
        valider_age(age) and
        valider_description(description) and
        valider_courriel(courriel) and
        valider_adresse(adresse) and
        valider_ville(ville) and
        valider_code_postal(code_postal)
    ):
        return True
    else:
        return False
