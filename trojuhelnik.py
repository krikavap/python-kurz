"""
trojuhelnik.py
Vytvoř program, který na vstupu získá 
přirozené číslo, a na výstupu vykreslí 
tvar rovnostranného trojúhelníku. 
Př.: 	vstup = 4
		výstup:
 
   o
  o o
 o o o
o o o o
 
"""

def trojuhelnik(cislo):
    for i in range(1, cislo+1):

        print(" "*(cislo - i) + "o " * i)
    
    pass

vstup = int(input("Zadej číslo: "))
trojuhelnik(vstup)