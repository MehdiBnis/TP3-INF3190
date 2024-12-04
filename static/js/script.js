// Front-end de l'application

function validerNom() {
    let nom = document.getElementById("nom").value;
    let erreurNom = document.getElementById("erreur-nom");

    if (nom.trim().length === 0) {
        erreurNom.innerHTML = "Veuillez entrer le nom de l'animal.";
        return false;
    } else if (nom.trim().length < 3 || nom.trim().length > 20) {
        erreurNom.innerHTML = "Le nom de l'animal doit avoir entre 3 et 20 caractères.";
        return false;
    } else if (nom.includes(',')){
        erreurNom.innerHTML = "L'entrée ne doit pas contenir de virgule.";
        return false;
    } else {
        erreurNom.innerHTML = "";
        return true;
    }
}

function validerEspece() {
    let espece = document.getElementById("espece").value;
    let erreurEspece = document.getElementById("erreur-espece");

    if (espece.trim().length === 0) {
        erreurEspece.innerHTML = "Veuillez entrer l'espèce de l'animal.";
        return false;
    } else if (espece.includes(',')){
        erreurEspece.innerHTML = "L'entrée ne doit pas contenir de virgule.";
        return false;
    } else {
        erreurEspece.innerHTML = "";
        return true;
    }
}

function validerRace() {
    let race = document.getElementById("race").value;
    let erreurRace = document.getElementById("erreur-race");

    if (race.trim().length === 0) {
        erreurRace.innerHTML = "Veuillez entrer la race de l'animal.";
        return false;
    } else if (race.includes(',')){
        erreurRace.innerHTML = "L'entrée ne doit pas contenir de virgule.";
        return false;
    } else {
        erreurRace.innerHTML = "";
        return true;
    }
}

function validerAge() {
    let age = document.getElementById("age").value;
    let erreurAge = document.getElementById("erreur-age");

    if (isNaN(age)) {
        erreurAge.innerHTML = "Veuillez entrer l'âge de l'animal.";
        return false;
    } else if (age.includes(',')) {
        erreurAge.innerHTML = "L'entrée ne doit pas contenir de virgule.";
    } else if (age < 0 || age > 30) {
        erreurAge.innerHTML = "L'âge doit être compris entre 0 et 30 ans.";
        return false;
    } else {
        erreurAge.innerHTML = "";
        return true;
    }
}

function validerDescription () {
    let description = document.getElementById("description").value;
    let erreurDescription = document.getElementById("erreur-description");

    if (description.trim().length === 0) {
        erreurDescription.innerHTML = "Veuillez entrer la description de l'animal.";
        return false;
    } else if (description.includes(',')) {
        erreurDescription.innerHTML = "L'entrée ne doit pas contenir de virgule.";
        return false;
    } else {
        erreurDescription.innerHTML = "";
        return true;
    }
}

function validerCourriel () {
    let courriel = document.getElementById("courriel").value;
    let erreurCourriel = document.getElementById("erreur-courriel");
    const regexCourriel = new RegExp("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])");

    if (courriel.trim().length === 0) {
        erreurCourriel.innerHTML = "Veuillez entrer votre adresse courriel.";
        return false;
    } else if (courriel.includes(',')) {
        erreurCourriel.innerHTML = "L'entrée ne doit pas contenir de virgule.";
        return false;
    } else if (!regexCourriel.test(courriel)) {
        erreurCourriel.innerHTML = "L'adresse courriel n'est pas valide (ex: exemple@courriel.com).";
        return false;
    } else {
        erreurCourriel.innerHTML = "";
        return true;
    }
}

function validerAdresse () {
    let adresse = document.getElementById("adresse").value;
    let erreurAdresse = document.getElementById("erreur-adresse");
    const regexAdresse = new RegExp("^\\d+\\s[0-9A-Za-z\\s]+$");

    if (adresse.trim().length === 0) {
        erreurAdresse.innerHTML = "Veuillez entrer votre adresse civile.";
        return false;
    } else if (adresse.includes(',')) {
        erreurAdresse.innerHTML = "L'entrée ne doit pas contenir de virgule.";
        return false;
    } else if (!regexAdresse.test(adresse)) {
        erreurAdresse.innerHTML = "L'adresse civile n'est pas valide (ex: 123 rue St Denis).";
        return false;
    } else {
        erreurAdresse.innerHTML = "";
        return true;
    }
}

function validerVille () {
    let ville = document.getElementById("ville").value;
    let erreurVille = document.getElementById("erreur-ville");

    if (ville.trim().length === 0) {
        erreurVille.innerHTML = "Veuillez entrer votre ville.";
        return false;
    } else if (ville.includes(',')) {
        erreurVille.innerHTML = "L'entrée ne doit pas contenir de virgule.";
        return false;
    } else {
        erreurVille.innerHTML = "";
        return true;
    }
}

function validerCodePostal () {
    let codePostal = document.getElementById("cp").value;
    let erreurCodePostal = document.getElementById("erreur-cp");
    const regexCodePostal = new RegExp("^[A-Za-z]\\d[A-Za-z][ -]?\\d[A-Za-z]\\d$");

    if (codePostal.trim().length === 0) {
        erreurCodePostal.innerHTML = "Veuillez entrer votre code postal.";
        return false;
    } else if (codePostal.includes(',')) {
        erreurCodePostal.innerHTML = "L'entrée ne doit pas contenir de virgule.";
        return false;
    } else if (!regexCodePostal.test(codePostal)) {
        erreurCodePostal.innerHTML = "Le code postal doit avoir un format canadien (ex: M5V 3L9).";
        return false;
    } else {
        erreurCodePostal.innerHTML = "";
        return true;
    }
}

function validerElements (action) {
    let nomValide = validerNom();
    let especeValide = validerEspece();
    let raceValide = validerRace();
    let ageValide = validerAge();
    let descriptionValide = validerDescription();
    let courrielValide = validerCourriel();
    let adresseValide = validerAdresse();
    let villeValide = validerVille();
    let cpValide = validerCodePostal();
    let elementsValides = nomValide && especeValide
                        && raceValide && ageValide
                        && descriptionValide && courrielValide
                        && adresseValide && villeValide
                        && cpValide;

    if (!elementsValides) {
        // Interrompre la soumission du formulaire interrompue s'il n'est pas validé
        action.preventDefault();
        document.getElementById("erreur-formulaire").innerHTML = "Champ(s) invalide(s).";
    }
    // Soumettre le formulaire
}

function validerFormulaire() {
    document.getElementById("nom").addEventListener("input", validerNom);
    document.getElementById("espece").addEventListener("input", validerEspece);
    document.getElementById("race").addEventListener("input", validerRace);
    document.getElementById("age").addEventListener("input", validerAge);
    document.getElementById("description").addEventListener("input", validerDescription);
    document.getElementById("courriel").addEventListener("input", validerCourriel);
    document.getElementById("adresse").addEventListener("input", validerAdresse);
    document.getElementById("ville").addEventListener("input", validerVille);
    document.getElementById("cp").addEventListener("input", validerCodePostal);

    document.getElementById("formulaire").addEventListener("submit", validerElements);
}

validerFormulaire();