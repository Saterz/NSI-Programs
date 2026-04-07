liste = [i * 0.5 for i in range(10)]

def rech_par_dichotomie(liste: list[float], elem: float):
    trouve = False
    position = None
    while trouve == False:
        n = len(liste)
        milieu = round(n / 2)
        if liste[milieu] < elem:
            print(f"Le milieu est plus petit que l'élément recherché : {liste[milieu]} < {elem}")
            liste = liste[milieu + 1:n]
            print(liste)
        elif liste[milieu] > elem:
            print(f"Le milieu est plus grand que l'élément recherché : {liste[milieu]} > {elem}")
            liste = liste[0:milieu]
            print(liste)
        elif liste[milieu] == elem:
            position = milieu
            trouve = True
    return position

print(liste)
print(rech_par_dichotomie(liste, 2.3))
