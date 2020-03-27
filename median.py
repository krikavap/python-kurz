"""
median.py
Vytvoř program, který na vstupu získá pole čísel a na výstupu 
vrátí jeho medián. Wikipedia: (...) stačí hodnoty seřadit podle
velikosti a vzít hodnotu, která se nalézá uprostřed seznamu. 
Pokud má soubor sudý počet prvků, obvykle se za medián označuje 
aritmetický průměr hodnot na místech n/2 a n/2+1.
"""
import random

def vytvorPole(pocet):
    pole = []
    for i in range(0, pocet):
        cislo = random.randint(1, 255)
        pole.append(cislo)
    
    return pole


hodnoty = []
pocetPrvkuPole = int(input("Zadej počet prvků pole hodnot: "))
hodnoty = vytvorPole(pocetPrvkuPole)
hodnoty.sort()

if pocetPrvkuPole % 2 == 0:
    med = (hodnoty[int((pocetPrvkuPole)/2)-1] + hodnoty[int((pocetPrvkuPole)/2)])/2
else:
    med = hodnoty[int((pocetPrvkuPole)/2)]

print(f"Medián pole {hodnoty} je {med} ")