import csv

retraites = []
with open(file="exercises/retraites/liste_retraites.csv") as fichier:
    reader = csv.DictReader(fichier, delimiter=";")
    for ligne in reader:
        retraites.append(ligne)


def moyenne_actif_toulouse(retraites):
    ages = []
    for retraite in retraites:
        if (
            retraite["commune_naissance"] == "Toulouse"
            and retraite["statut"] == "activité"
        ):
            ages.append(int(retraite["age"]))
    return sum(ages) / len(ages)


print(moyenne_actif_toulouse(retraites))
