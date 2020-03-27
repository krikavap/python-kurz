"""
vypisCisel.py

pomocí cyklu vypíše čísla od -x do +x. x zadá uživatel na vstupu
čísla budou formátována:
záporná se dvěmi desetinnými místy
nula a kladná zarovnaná doprava a s předřazenými nulami
"""

cislo = int(input("zadej číslo:"))

zacatek = cislo * (-1)
konec = cislo

for cislo in range(zacatek, konec +1):
    if cislo < 0:
        print(f"{cislo:>6.2f}")
    else:
        print(f"{cislo:>06.2f}")
