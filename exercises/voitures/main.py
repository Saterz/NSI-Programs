import csv

voitures = []
with open("voitures.csv", encoding="utf-8") as fichier:
    reader = csv.DictReader(fichier, delimiter=";")
    for ligne in reader:
        voitures.append(ligne)

"""
Nombres de voitures électriques de marque Renault fabriqués en 2004
"""
def renault_electriques_2004(voitures):
    nbr = 0
    for voiture in voitures:
        if voiture["marque"] == "Renault" and voiture["année"] == "2004" and voiture["énergie"] == "Électrique":
            nbr += 1
    return nbr

print(renault_electriques_2004(voitures))


"""
Nombres de voitures de la marque Ford roulant avec de l'essence et du gasoil
"""
def ford_thermique(voitures):
    nbr = 0
    for voiture in voitures:
        if voiture["marque"] == "Ford" and (voiture["énergie"] == "Diesel" or voiture["énergie"] == "Essence"):
            nbr += 1
    return nbr

print(ford_thermique(voitures))

"""
Nombres de voitures électriques produits entre 2004 et 2010
"""
def elec_prd_2004_2010(voitures):
    nbr = 0
    for voiture in voitures:
        if voiture["année"] >= "2004" and voiture["année"] <= "2010" and voiture["énergie"] == "Électrique":
            nbr += 1
    return nbr

print(elec_prd_2004_2010(voitures))

"""
Nombres de Clio jaune produits en 2018
"""
def clio_jaune_2018(voitures):
    nbr = 0
    for voiture in voitures:
        if voiture["année"] == "2018" and voiture["model"] == "Clio" and voiture["couleur"] == "Jaune":
            nbr += 1
    return nbr

print(clio_jaune_2018(voitures))
