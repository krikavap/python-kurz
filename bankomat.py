"""
bankomat.py

program částku na vstupu rozdělí na mince nominálních hodnot 50, 20, 10, 5, 2, 1

vstup: částka, která se má dělit
výstup: počet mincí jednotlivých nominálních hodnot

nově doplněno i ošetření chybových stavů při zadání částky a přesunutí výpočtu do funkce

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

def vypocet(penez):
    
    # 2. výpočet
    padesat=penez//50
    penez=penez%50

    dvacet=penez//20
    penez=penez%20

    deset=penez//10
    penez=penez%10

    pet=penez//5
    penez=penez%5

    dva=penez//2
    penez=penez%2

    jedna=penez//1
    penez=castka%1

    return padesat, dvacet, deset, pet, dva, jedna


# 1. zadání částky do proměnné castka

castka = 0
    
castka=input("Zadej částku (celé kladné číslo):")
try:
    castka = int(castka)
    if castka > 0: 
        x = vypocet(castka)
        # 3. výpis výsledků
        print("výsledek:", "\n", "50:",x[0],"\n", "20:", x[1],"\n", "10:", x[2], "\n", "5:", x[3], "\n", "2:", x[4],"\n", "1:", x[5],"\n")
    else:
        print("zadané číslo musí být > 0")

except TypeError:
    print("TypeError: Celé číslo musíš zadat! ")
except ValueError:
    print("Celé číslo musíš zadat! ")
finally:
    print()