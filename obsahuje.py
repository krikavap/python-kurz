"""
obsahuje.py

načte řetězec obsahující znaky a číslice
prochází řetězec a rozděluje znaky do skupin: písmena, číslice, jiné znaky
vypíše kolik znaků obsahuje každá skupina

načte nový znak. pokud se v řetězci nevyskytuje, přidá jej na konec řetězce
a celý řetězec vypíše na obrazovku

"""
pocet_pismen = 0
pocet_cisel = 0
pocet_jine = 0

retezec = str(input("zadej libovolný řetězec: "))

delka = len(retezec)

print()
print(f"Počet písmen v řetězci: {delka}")

for i in range(0, delka):
    if retezec[i].isalpha():
        pocet_pismen = pocet_pismen + 1
    else:
        if retezec[i].isdigit():
            pocet_cisel = pocet_cisel + 1
        else:
            pocet_jine = pocet_jine + 1

print("V řetězci je:")
print(f"Písmen: {pocet_pismen:>}")
print(f"Čísel: {pocet_cisel:>}")
print(f"Dalších znaků: {pocet_jine:>}")

dalsi_znak = str(input("Zadej další znak: "))

#if retezec.find(dalsi_znak)== -1:      #jeden způsob
if dalsi_znak not in retezec:           # druhý možný způsob
    pass
    retezec = retezec + dalsi_znak
    print(f"Zadaný znak byl přidán na konec řetězce. Nový řetězec je \"{retezec}\".")
else:
    print(f"Zadaný znak již v řetězci \"{retezec}\" existuje.")
