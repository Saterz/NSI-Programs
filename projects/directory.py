# Emplacement du fichier
file_dir = "./annuaire.txt"

# Séparateur pour esthétique
seperator = "-"

# Message d'erreur général
error = "Une erreur est survenue. Merci de réessayer"

def clean(text):
    """
    Nettoie le texte de caractères inutiles et met tout en minuscule
    """
    return text.strip().replace("-", "").replace(" ", "").lower()

def parse(name, number):
    """
    Permet de mettre le nom et le numéro sous une forme correcte pour l'annuaire
    """
    return name + " " + seperator + " " + number

def add_in_dir(file, text):
    """
    Ajoute le texte dans l'annuaire et un séparateur pour l'esthétique
    """
    file.write(f"{text}\n{seperator * 38}\n")

def search_in_dir(file, text):
    """
    Cherche le texte donné dans l'annuaire 
    """
    found = []
    for line in file:
        line_cln = clean(line)
        if text in line_cln:
            found.append(line)
    return found

def main():
    """
    Boucle principale du programme
    """
    
    # Affichage du menu
    print(f"Bienvenue dans l'annuaire !\n{seperator * 28}\nQue voulez vous faire aujourd'hui ?\n1- Ajouter un contact à l'annuaire\n2- Chercher un contact dans l'annuaire\n0- Quitter\n{seperator * 39}")
    
    # Boucle infini pour recommencer au cas d'une erreur
    while True:
        # Essaye de transformer la requète de l'utilisateur en type entier
        try:
            task = int(input("Choisissez un numéro : "))
        # Si erreur afficher le texte d'erreur
        except:
            print(error)
        else:
            print(seperator * 39)
            match task:
                case 0:
                    print("Merci d'avoir utilisé l'annuaire !")
                    break
                case 1:
                    try:
                        print("Quel est le nom et le numéro de la personne que vous voullez ajouter ?")
                        name = str(input("Nom : "))
                        number = str(input("Numéro : "))
                    except:
                        print(error)
                    else:
                        parsed = parse(name, number)
                        with open(file_dir, "a", encoding="utf-8") as file:
                            try:
                                add_in_dir(file, parsed)
                            except:
                                print(error)
                            else:
                                print("Contact ajouté avec succès !")
                    break
                case 2:
                    try:
                        print("Chercher le nom ou le numéro pour trouver les informations complémentaires")
                        query = str(input("Recherche : "))
                    except:
                        print(error)
                    else:
                        not_found = "Aucun résultat n'a été trouvé"
                        with open(file_dir, "r", encoding="utf-8") as file:
                            try:
                                cleaned = clean(query)
                                results = search_in_dir(file, cleaned)
                            except:
                                print(error)
                            else:
                                if len(results) <= 0 or len(cleaned) <= 0:
                                    return print(not_found)
                                
                                for result in results:
                                    print(result)
                    break
                case _:
                    print(error)


if __name__ == "__main__":
    main()


