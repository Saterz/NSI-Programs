# Calcul de factorielle

# Séparateur pour ajouter du visuel au programme
separateur = "------------------------"


def saisie():
    """
    Demande le chiffre à l'utilisateur
    """
    return input("Entrer le nombre: ")


# Calcul de la factorielle
def factorielle(nombre):
    """
    Calcule la factorielle
    """
    print("Calcul...", end="", flush=True)
    resultat = 1
    for chiffre in range(nombre):
        resultat = resultat * (chiffre + 1)
    print("\r" + " " * 50 + "\r", end="", flush=True)
    return resultat


# Si le programme est exécuter par l'utilisateur
if __name__ == "__main__":
    print("Calcul de factorielle")
    print(separateur)
    print("Indiquer le nombre pour calculer la factorielle")
    while True:
        try:
            nbrUtilisateur = int(saisie())
        except Exception as e:
            print("\nLa valeur donné n'est pas un nombre, merci de réessayer")
            print(separateur)
        else:
            print(separateur)
            print("La réponse est:", factorielle(nbrUtilisateur))
            break
