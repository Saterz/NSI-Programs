from random import randint

def sort(liste: list[int]) -> list[int]:
    sorted: list[int] = liste
    for _ in range(len(liste)):
        for index in range(len(sorted)):
            pre_index = max(index - 1, 0)
            last = liste[pre_index]
            current = liste[index]
            if current < last:
                liste[pre_index] = current
                liste[index] = last
    return sorted

liste_aleatoire = [randint(1, 100) for _ in range(10)]
print("Initial list:", liste_aleatoire)
print("Sorted list:", sort(liste_aleatoire))