"""
palindrom.py

program vyhodnotí, zda je dané slovo palindrom (slovo, které je zapředu a zezadu stejné)
"""

slovo = str(input("Zadej slovo: "))
slovo = slovo.lower()
delka = len(slovo)
zacatek = -1
konec = delka - 1
krok = -1
slovo_pozpatku = ""

for i in range(konec, zacatek, krok):
    slovo_pozpatku = slovo_pozpatku + slovo[i]

if slovo == slovo_pozpatku:
    print (f"Slovo {slovo} je palindrom (stejné při čtení zepředu i zezadu)")
else:
    print (f"Slovo {slovo} palindrom není. ")
