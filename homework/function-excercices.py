from time import sleep
from math import pi

# Objectifs
# - Comprendre comment déclarer une fonction
# - Passer des arguments à une fonction
# - Retourner des valeurs
# - Utiliser des fonctions dans un programme

# Exercice 1 : Bonjour !
def dire_bonjour():
    print("Bonjour !")


# Exercice 2 : Bonjour à toi !
def dire_bonjour_prenom(name):
    print(f"Bonjour, {name} !")


# Exercice 3 : Carré d’un nombre
def carre(number):
    print(number**2)


# Exercice 4 : Addition
def addition(a, b):
    print(a + b)


# Exercice 5 : Est pair ?
def est_pair(number):
    if number / 2 == 0:
        return True

    return False


# Exercice 6 : Afficher un encadré
def afficher_encadre(msg):
    sep = "*"
    taille = len(msg) + 4
    print(sep * (taille))
    print(f"{sep} {msg} {sep}")
    print(sep * (taille))


# Exercice 7 : Convertir Celsius → Fahrenheit
def convertir_celsius_en_fahrenheit(cel):
    return cel * 9 / 5 + 32


# Exercice 8 : Compteur décroissant
def compte_a_rebours(n):
    for i in range(n, 0, -1):
        print(i)
        sleep(1)

    print("Go !")


# Exercice 9 : Mot de passe valide
def mot_de_passe_valide(mdp):
    if len(mdp) >= 8:
        return True

    return False


# Exercice 10 : Calculer l’aire d’un cercle
def aire_cercle(r):
    return pi * r**2


# 🔧 Exercices : Corriger les erreurs dans des fonctions

# Exercice 1 : Bonjour le prénom
# def dire_bonjour_prenom_2:
#   print("Bonjour", prenom)


def dire_bonjour_prenom_2(prenom):
    print("Bonjour", prenom)


# Exercice 2 : Cube d’un nombre
# def cube(x):
# return x * x * x


def cube(x):
    return x**3


# Exercice 3 : Vérifier si un nombre est négatif
# def est_negatif(nombre):
#   if nombre < 0:
#       True
#   else:
#       False


def est_negatif(nombre):
    if nombre < 0:
        return True
    else:
        return False


# Exercice 4 : Multiplier deux nombres
# def multiplier(a, b)
#   resultat = a * b
#   return resultat


def multiplier(a, b):
    resultat = a * b
    return resultat


# Exercice 5 : Convertir des minutes en secondes
# def convertir_minutes_en_secondes(minutes):
#   return minutes * 60
#   print("Conversion terminée")


def convertir_minutes_en_secondes(minutes):
    secondes = minutes * 60
    print("Conversion terminée")
    return secondes


# Exercice 6 : Afficher une salutation
# def saluer(nom)
#   message = "Salut " + nom
#   return message
#   print(message)


def saluer(nom):
    message = "Salut " + nom
    return message


# Exercice 7 : Division protégée
# def division(a, b):
#   if b != 0:
#       return a / b
#   else:
#       "Impossible de diviser par zéro"


def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Impossible de diviser par zéro")


# Exercice 8 : Nombre est-il égal à 10 ?
# def est_dix(n):
#   if n = 10:
#       return True
#   else:
#       return False

def est_dix(n):
  if n == 10:
      return True
  else:
      return False

# Exercice 9 : Retourner la plus grande valeur
# def max_deux(a, b):
#   if a > b:
#       return a
#   if b > a:
#       return b

def max_deux(a, b):
  if a > b:
      return a
  if b > a:
      return b
  if a == b:
      return a

# Exercice 10 : Compter jusqu’à n
# def compter(n):
#   i = 1
#   while i <= n:
#       print(i)

def compter(n):
    i = 1
    while i <= n:
        i =+ 1
        print(i)
