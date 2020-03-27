"""
znamky2.py

do programu lze zadávat známky od 1 do 5
pokud uživatel zadá mimo rozsah, program je ukončen

modifikace - známky jsou ukládány do seznamu, seznam je vypsán, následně setříděn a znovu vypsán
použity funkce pro práci se seznamy

"""
seznam=[]
znamka = (int(input("Zadej 1. známku: ")))

while znamka in range(1,6):     # cyklus běží pro všechny známky v rozsahu 1-5
    seznam.append(znamka)
    znamka = (int(input(f"Zadej {len(seznam)+1}. známku: ")))

print(f"Počet zadaných známek: {len(seznam)}")
if len(seznam)>0:
    print(seznam)
    seznam.sort()
    print(seznam)

    print(f"Průměr zadaných známek: {sum(seznam)/len(seznam):>4.2f}")
    print(f"Nejlepší známka: {min(seznam)}")
    print(f"Nejhorší známka: {max(seznam)}")
