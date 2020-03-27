"""
znamky.py

do programu lze zadávat známky od 1 do 5
pokud uživatel zadá mimo rozsah, program je ukončen
následně vypíše, kolik známek bylo zadáno, jaká byla nejlepší, jaká nejhorší a dosažený průměr

"""
znamka = int(input("Zadej 1. známku: "))

# iniciace proměnných
pocet = 0
maximum = znamka
minimum = znamka
soucet = 0

while znamka in range(1,6):     # cyklus běží pro všechny známky v rozsahu 1-5
    pocet = pocet + 1
    soucet = soucet + znamka
    if maximum < znamka:
        maximum = znamka
    elif minimum > znamka:
        minimum = znamka
    znamka = int(input(f"Zadej {pocet + 1}. známku: "))

if pocet == 0:  # ošetření dělení 0
    print()
    print("Nezadal jsi žádnou známku v rozsahu 1 - 5.")
else:
    print()
    print(f"Zadal jsi {pocet} známek se součtem {soucet} a s průměrem {soucet / pocet:4.2f}")
    print(f"Nejlepší známka byla {minimum} a nejhorší byla {maximum}")
