"""
cisla.py

uživatel postupně zadává čísla. ukončení zadávání znakem 0
spočítá jejich Součet, průměr, maximum a minimum

"""
cislo = int(input("Zadej kladné celé číslo. Zadávání ukonči nulou: "))
soucet = 0
maximum = cislo
minimum = cislo
pocet = 0

"""
while cislo != 0:
    cislo = int(input("Zadej kladné celé číslo. Zadávání ukonči nulou: "))
    if cislo > 0:
        soucet = soucet + cislo
        pocet = pocet + 1
        if cislo > maximum:
            maximum = cislo
        if cislo < minimum:
            minimum = cislo
"""
while cislo != 0:
    pocet = pocet + 1
    soucet = soucet + cislo
    if cislo > maximum:
        maximum = cislo
    if cislo < minimum:
        minimum = cislo
    cislo = int(input("Zadej kladné celé číslo. Zadávání ukonči nulou: "))


if pocet > 0:
    print(f"Součet: {soucet}")
    print(f"Počet čísel: {pocet}")
    print(f"Průměr: {soucet/pocet}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
