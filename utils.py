import random as rnd
import string

LETTERS = list(string.ascii_lowercase)

def create_lvl(difficult: int)->list:
    lvl = []
    for _ in range(difficult):
        lvl.append(rnd.choice(LETTERS))
    return lvl