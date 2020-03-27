"""
dedictvi.py

algoritmus pro rozdělení majetku mezi libovolný počet potomků
každý dostane stejnou částku + zůstane nerozdělený zbytek

vstup: částka k rozdělení, počet potomků
výstup: částka na jednoho potomka a výše nerozděleného zbytku
"""

castka = int(input("Zadej částku, která se bude rozdělovat: "))
potomci = int(input("Zadej počet potomků: "))

if potomci > 0:
    castka_rozdelit = castka // potomci
    zbytek = castka % potomci
    print(f"Každý potomek dostane {castka_rozdelit:,.2f} Kč. Nerozdělený zbytek činí {zbytek:,.2f} Kč.")
else:
    print("Nutno zadat počet potomků!")
