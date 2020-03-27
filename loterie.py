"""
loterie.py

program vygeneruje 7 náhodných unikátních čísel v rozsahu 1 - 49
čísla budou uložena v seznamu a seřazena od nejmenšího po největší

"""
import random

pocet = 7
seznam = []
i = 1

while i <= pocet:
    cislo = random.randint(1, 49)
    if cislo not in seznam:
        i = i + 1
        seznam.append(cislo)


print(seznam)   # tisk původní seznam
seznam.sort()   # seřazení seznamu
print(seznam)
random.shuffle(seznam)  # náhodné přetřídění
print(seznam)
