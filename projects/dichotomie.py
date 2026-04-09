liste = [i * 0.5 for i in range(999)]

def rech_par_dichotomie(liste: list[float], elem: float)-> int | None:
    debut: int = 0
    fin: int = len(liste) - 1
    while debut <= fin:
        milieu: int = (debut + fin) // 2
        if liste[milieu] < elem:
            debut = milieu + 1
        elif liste[milieu] > elem:
            fin = milieu - 1
        else:
            return milieu
    return None

print(rech_par_dichotomie(liste, 100))