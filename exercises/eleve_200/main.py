import csv

eleves = []
with open('exercises/eleve_200/eleves_200.csv', encoding="utf-8") as fichier:
    reader = csv.DictReader(fichier, delimiter=";")
    for ligne in reader:
        eleves.append(ligne)

print(eleves)

def moins_de_13(eleves):
    filtre = []
    for eleve in eleves:
        if int(eleve["age"]) < 13:
            filtre.append(eleve["prenom"])
    return filtre

def filles_plus_de_14(eleves):
    nbr = 0
    for eleve in eleves:
        if eleve["sexe"] == "F" and int(eleve["age"]) > 14:
            nbr += 1
    return nbr

def garcon_espagnol(eleves):
    filtre = []
    for eleve in eleves:
        if eleve["sexe"] == "M" and eleve["lv2"] == "Espagnol":
            filtre.append(eleve["prenom"])
    return filtre

def filles_plus_de_14_allemand(eleves):
    nbr = 0
    for eleve in eleves:
        if eleve["sexe"] == "F" and int(eleve["age"]) > 14 and eleve["lv2"] == "Allemand":
            nbr += 1
    return nbr

def garcon_toulouse(eleves):
    nbr = 0
    for eleve in eleves:
        if eleve["sexe"] == "M" and eleve["commune_naissance"] == "Toulouse":
            nbr += 1
    return nbr

def famille_martin(eleves):
    filtrer = []
    for eleve in eleves:
        if eleve["nom"] == "Martin":
            filtrer.append(eleve["prenom"])
    return filtrer


print(moins_de_13(eleves))
print(filles_plus_de_14(eleves))
print(garcon_espagnol(eleves))
print(filles_plus_de_14_allemand(eleves))
print(garcon_toulouse(eleves))
print(famille_martin(eleves))
