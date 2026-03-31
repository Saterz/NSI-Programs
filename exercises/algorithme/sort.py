from random import randint

def sort(liste: list[int]) -> list[int]: # 6n^2+2n+2 = O(n^2) 
    sorted = liste.copy()
    for _ in range(len(sorted)): # n
        for index in range(len(sorted)): # n
            pre_index: int = max(index - 1, 0) # n^2
            last: int = sorted[pre_index] # n^2
            current: int = sorted[index] # n^2
            if current < last: # n^2
                sorted[pre_index] = current # n^2
                sorted[index] = last # n^2
    return sorted # 1

liste_aleatoire = [randint(1, 100) for _ in range(10)]
print("Initial list:", liste_aleatoire)
print("Sorted list:", sort(liste_aleatoire))