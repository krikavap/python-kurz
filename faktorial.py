"""
faktorial.py

využití funkce pro výpočet faktorialu přirozeného čísla

využívá math
"""

import math

cislo=int(input("zadej celé kladné číslo:"))


#cele_cislo = int(cislo)

# test, zda číslo je přirozené

if cislo < 0:
    print("Chyba: Zadané číslo není kladné")
else:
    faktorial = math.factorial(cislo)       # výpočet
    print(f"Faktoriál z čísla {cislo:>}! = {faktorial}")
    pass
