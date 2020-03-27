"""
trideniASCII.py

program roztřídí ascii tabulku na písmena, cifry a další znaky
vypíše počet znaků v každé skupině a obsah skupiny

"""
pismena = ""
cifry = ""
ostatni = ""

for i in range(0,128):
    znak = chr(i)
    if znak.isdigit():
        cifry = cifry + znak
    else:
        if znak.isalpha():
            pismena = pismena + znak
        else:
            ostatni = ostatni + znak

pocet_pismen = len(pismena)
pocet_cisel = len(cifry)
pocet_jine = len(ostatni)

print()
print("ASCII TABULKA MÁ:")
print(f" Počet písmen: {pocet_pismen:>3}")
print(f"  Počet čísel: {pocet_cisel:>3}")
print(f"Počet ostatní: {pocet_jine:>3}")
print(f"       CELKEM: {pocet_pismen + pocet_cisel + pocet_jine:>3}")

print()
print(f"Písmena: \n{pismena}\n")
print(f"Čísla: \n{cifry}\n")
print(f"Ostatní znaky: \n{ostatni}")
