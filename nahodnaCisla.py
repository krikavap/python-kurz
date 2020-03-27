"""
nahodnaCisla.py

"""

import random

cislo = random.random()     # generuje náhodné desetinné číslo mezi 0 - 1
print(cislo)

cislo = random.randint(1, 154)   # generuje náhodná celá čísla v intervalu v závorce
print(cislo)

# generuje náhodná celá čísla v intervalu v závorce, poslední číslo je krok, jehož násobky může generátor vybrat jako náhodné číslo
cislo = random.randrange(1, 49, 7)
print(cislo)

sekvence = (1,5,6,7)
cislo = random.choice(sekvence)     # náhodně vybere z definované sekvence nebo řetězce
print(cislo)

seznam = []
seznam.extend(["první", "druhá", "třetí"])
random.shuffle(seznam)      # náhodně promíchá seznam
print(seznam)

print(random.sample(seznam, 2))     # náhodně vybere definovaný počet prvků ze seznamu (zde 2)
