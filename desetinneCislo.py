"""
desetinneCislo.py

program rozdělí desetinné číslo na celou a desetinnou část

vstup: desetinné číslo
výstup: přirozené číslo a desetinná část

postup:
1. zadání čísla -> proměnná cislo
2. výpočet:
    a. celočíselné dělení -> proměnna cele_cislo
    b. zbytek -> proměnná zbytek
3. výpis výsledků
"""

# 1. zadání čísla
cislo=float(input("zadej desetinné číslo:"))

# 2. výpočet
cele_cislo=cislo//1
zbytek=cislo%1

# 3. výpis výsledků
print(" celá část:", cele_cislo,"\n", "desetinná část:", zbytek)


"""
druhý způsob

postup:
1. zadání čísla -> proměnná cislo
2. výpočet:
    a. celočíselné dělení -> proměnna cele_cislo
    b. zbytek -> proměnná zbytek = cislo-cele_cislo
3. výpis výsledků
"""


# 2. výpočet
cele_cislo=cislo//1
zbytek=cislo-cele_cislo

# 3. výpis výsledků
print(" celá část:", cele_cislo,"\n", "desetinná část:", zbytek)


"""
třetí způsob - využití knihovny math

"""
import math

zbytek2,cele_cislo2 = math.modf(cislo)
print("pomocí funkce math.modf()")
print(" celá část:", cele_cislo2,"\n", "desetinná část:", zbytek2)
