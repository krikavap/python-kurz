"""
matematika.py
Vytvoř dvě funkce, které budeš volat na vložené číslo.
 
funkce „fibonacci“
Vytvoř funkci, která vypíše prvních „x“ prvků Fibonacciho posloupnosti.
 
funkce „faktorial“
Vytvoř funkci, která vrátí vypočítaný faktoriál vloženého čísla „x“.
"""

import math

def faktorialCisla(zaklad):
    pass
    faktorial = math.factorial(zaklad)       # výpočet
    print(f"Faktoriál z čísla {zaklad:>}! = {faktorial}")

def fibonacci(pocet):
    
    a = 0
    b = 1
    i = 0
    soucet = 0
    fiboSeznam = []
    fiboSeznam.append(a)
    fiboSeznam.append(b)

    while i < pocet:
        soucet = a + b
        fiboSeznam.append(soucet)
        a = b
        b = soucet
        i = i + 1
    print(f"Fabonacciho posloupnost je {fiboSeznam}")

cislo=int(input("zadej celé kladné číslo:"))


#cele_cislo = int(cislo)

# test, zda číslo je přirozené

if cislo < 0:
    print("Chyba: Zadané číslo není kladné")
else:
    faktorialCisla(cislo)
    fibonacci(cislo)