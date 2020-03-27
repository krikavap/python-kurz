"""
bankomat.py

program částku na vstupu rozdělí na mince nominálních hodnot 50, 20, 10, 5, 2, 1

vstup: částka, která se má dělit
výstup: počet mincí jednotlivých nominálních hodnot

postup:
1. zadání částky do proměnné castka
2. výpočet:
    a. částku vydělím 50, výsledek uložím do proměnné padesat
    b. zbytek vydělím 20, výsledek uložím do proměnné dvacet
    b. zbytek vydělím 10, výsledek uložím do proměnné deset
    b. zbytek vydělím 5, výsledek uložím do proměnné pet
    b. zbytek vydělím 2, výsledek uložím do proměnné dva
    b. zbytek vydělím 1, výsledek uložím do proměnné jedna
3. výpis výsledků
"""
# 1. zadání částky do proměnné castka
castka=int(input("zadej částku:"))
castka_puvodni=castka

# 2. výpočet
padesat=castka//50
castka=castka%50

dvacet=castka//20
castka=castka%20

deset=castka//10
castka=castka%10

pet=castka//5
castka=castka%5

dva=castka//2
castka=castka%2

jedna=castka//1
castka=castka%1

# 3. výpis výsledků
print("výsledek:", "\n", "50:",padesat,"\n", "20:", dvacet,"\n", "10:", deset, "\n", "5:", pet, "\n", "2:", dva,"\n", "1:", jedna,"\n")
