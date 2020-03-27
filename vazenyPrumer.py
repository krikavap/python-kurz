"""
vazenyPrumer.py
Vytvoř program, který na vstupu získá dvě 
stejně velká pole -- hodnoty a k nim 
odpovídající váhy. Na výstupu vypíše 
hodnotu váženého průměru. 
"""
import random

def vytvorPole(pocet):
    pole = []
    for i in range(0, pocet):
        cislo = random.randint(1, 255)
        pole.append(cislo)
    
    return pole

def VazenyPrumerPole(pole, vaha):
    suma = 0
    for i in range(0, len(pole)):
        suma = suma + (pole[i] * vaha[i])
    prumer = suma / sum(vaha)
    return prumer

hodnoty = []
vahy = []
pocetPrvkuPole = int(input("Zadej počet prvků pole hodnot: "))
hodnoty = vytvorPole(pocetPrvkuPole)
vahy = vytvorPole(pocetPrvkuPole)
prumerVazeny = VazenyPrumerPole(hodnoty, vahy)
prumerAritmeticky = sum(hodnoty)/len(hodnoty)


print(f"Pole {hodnoty}, váhy {vahy} vážený průměr {prumerVazeny}, aritmetický průměr je {prumerAritmeticky} ")
