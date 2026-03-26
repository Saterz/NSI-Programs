def toutes_occurr(liste: list[int], elem: int)-> list[int]: # 2n + 3 = O(n)
    n: int = len(liste) # 1
    positions: list[int] = [] # 1
    for i in range(n): # n
        if liste[i] == elem: # n
            positions.append(i) # 0
    return positions # 1
