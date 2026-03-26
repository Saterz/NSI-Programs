def premi_occu(liste: list[int], elem: int)-> int | None: # 3n + 5 = O(n)
    n: int = len(liste) # 1
    position: int | None = None # 1
    i = 0 # 1
    while i < n and position == None: # n + 1
        if liste[i] == elem: # n
            position = i # 0
        else:
            i += 1 # n
    return position # 1
