import csv

def verifie_quantites(donnes):
    for ligne in donnes:
        if int(ligne["qté"]) < 0:
            return False
    return True

def verifie_une_quantites(ligne):
    if int(ligne["qté"]) < 0:
        return False
    return True

def nombre_produit(donnes):
    tot = 0
    for ligne in donnes:
        if verifie_une_quantites(ligne):
            tot += int(ligne["qté"])
    return tot

donnes = []
with open("bon_de_commande.csv", encoding="utf-8", newline="") as fichier:
    reader = csv.DictReader(fichier, delimiter=";")
    for ligne in reader:
        donnes.append(dict(ligne))

print(verifie_quantites(donnes))
print(nombre_produit(donnes))
