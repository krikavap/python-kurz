"""
sudaLicha.py

vyhodnocuje, zda se jedná o sudé nebo liché číslo

"""
cislo = int(input("zadej celé číslo:"))

vysledek = cislo % 2
print(vysledek)
if vysledek == 0:
    print(f"Zadané číslo {cislo:,} je sudé")
else:
    print(f"Zadané číslo {cislo:,} je liché")
