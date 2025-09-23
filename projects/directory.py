from io import TextIOWrapper

seperator = "------------------------------------------"


def parse(name: str, number: str) -> str:
    sep = " - "
    parsed = name + sep + number
    return parsed


def add_to_dir(file: TextIOWrapper, name: str, number: str) -> bool:
    try:
        parsed = parse(name, number)
    except:
        print("Une erreur est survenu")
        return False
    file.read()
    file.write(f"{parsed}\n")
    return True


def search_in_dir(file: TextIOWrapper, name: str) -> str:
    for line in file:
        if name in line:
            return line


if __name__ == "__main__":
    file = open(
        "C:/Users/eleves/Documents/i 1 nsi/annuaire.txt", "r+", encoding="utf-8"
    )

    print(
        f"Bienvenue dans l'annuaire.\n{seperator}\nQue voullez vous faire ?\n1- Ajouter quelqu'un dans le répertoire\n2- Lire dans l'annuaire\n{seperator}"
    )
    query = int(input("Entrer un numéro: "))

    print(seperator)

    match query:
        case 1:
            print(
                "Veillez entrer le nom est numéro de la personne que vous voulez acheter"
            )
            name = input("Entrer le nom: ")
            number = input("Entrer son numéro: ")
            output = add_to_dir(file, name, number)
            if output == False:
                print("Une erreur est survenu")
            else:
                print("Ajouté avec succès!")
        case 2:
            query = input(
                "Entrer le nom de la personne dont vous voulez trouver le numéro: "
            )
            output = search_in_dir(file, query)
            print(output)
        case _:
            print("Vous n'avez pas donner un bon numéro")
