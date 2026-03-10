from typing import List

def is_present(list: List[int], number: int):
    is_present = False
    for elem in list:
        if elem == number:
            is_present = True
    return is_present

print(is_present([5,7,6,2,54,9,52,6,8,6,9,5,23,65,4,32,12,6,1,5,3,2,2523], 25))
