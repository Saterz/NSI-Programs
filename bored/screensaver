from random import randint
import time

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "123456789"
string = "|" + " " * 112 + "|"

def print_at_pos(position, string1, string2):
    output = string1[:position] + string2 + string1[position:]
    return output

while 1:
    either = randint(1, 2)
    pos = randint(1, len(string))
    letter = randint(0, len(alpha) - 1)
    number = randint(0, len(nums) - 1)
    if either == 1:
        print(print_at_pos(pos, string, alpha[letter]))
    else:
        print(print_at_pos(pos, string, nums[number]))
    time.sleep(0.1)
