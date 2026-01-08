###
# ACTIVITES LES SEQUENCES.pdf
###

# Activité 2.1
mon_tuple = (5, 8, 6, 9)
print(mon_tuple) # (5, 8, 6, 9)

# Activité 2.2
mon_tuple = (5, 8, 6, 9)
a = mon_tuple[1]
print(a) # 8

# Activité 2.3
a, b = (8, 5)
print(a) # 8
print(b) # 5

# Activité 2.4
mon_tab = [5, 8, 6, 9]
mon_tab[0] = 15
print(mon_tab) # [15, 8, 6, 9]

# Activité 2.5
tab = [3, 3, 6, 9]
tab.append(0)
print(tab) # [3, 3, 6, 9, 0]

# Activité 2.6
mon_tab = [1, 2, 3, 4]
del mon_tab[1]
print(mon_tab) # [1, 3, 4]

# Activité 2.7
mon_tab = [5, 8, 6, 9, 15, 0]
a = len(mon_tab)
print(a) # 6

# Activité 2.8
tab = [1, 2, 3]
s = 0
for t in tab:
    s = s + t
print(s) # 6

# Activité 2.9
tab = [5, 3, 4, 8]
mon_tab = [2*t for t in tab if t > 4]
print(mon_tab) # [10, 16]

# Activité 2.10
m = [[1, 3, 4], [5, 6, 8], [2, 1, 3], [7, 8, 15]]
a = m[0][1]
print(a) # 3

# Activité 2.11
m = [[1, 3], [5, 8], [2, 3]]
nb_colonne = 2
nb_ligne = 2
a = 0
for i in range(0, nb_ligne):
    for j in range(0, nb_colonne):
        a = a + m[i][j]
print(a) # 17

# Activité 2.12
def recherche_max(tab):
    maxi = 0
    for t in tab:
        if t > maxi:
            maxi = t
    return maxi
print(recherche_max([4, 3, 0, 5])) # 5

# Activité 2.13
def somme(tab):
    s = 0
    for t in tab:
        s = s + t
    return s
print(somme([3, 5, 8, 4])) # 20

# Activité 2.14
def recherche(tab, n):
    indice = -1
    for i, t in enumerate(tab):
        if n == t:
            indice = i
    return indice
print(recherche([3, 5, 8, 34], 8))
