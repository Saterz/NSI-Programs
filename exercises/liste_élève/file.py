import csv

listeeleves: list[dict[str, str]] = []
with open("exercises/liste_élève/liste_eleve.csv", encoding="utf-8") as fichier:
    reader = csv.DictReader(fichier, delimiter=";")
    for ligne in reader:
        listeeleves.append(dict(ligne))

def eleve_age(listeeleves: list[dict[str, str]], age: int) -> list[str]:
    eleves: list[str] = []
    for tab in listeeleves:
        if int(tab["age"]) == age:
            eleves.append(tab["prenom"] + " " + tab["nom"])
    return eleves

print(eleve_age(listeeleves, 17))

def eleves_nsi(listeeleves: list[dict[str, str]]) -> list[str]:
    eleves: list[str] = []
    spe = "NSI"
    for tab in listeeleves:
        if tab["sp1"] == spe:
            eleves.append(tab["prenom"] + " " + tab["nom"])
        elif tab["sp2"] == spe:
            eleves.append(tab["prenom"] + " " + tab["nom"])
    return eleves

print(eleves_nsi(listeeleves))