"""
pyramida.py
Vytvoř program, který dle vloženého 
přirozeného čísla vykreslí pyramidu.
Př.: 	vstup = 3
		výstup:
 
o
o o
o o o
 
"""

def pyramida(cislo):
    for radek in range(1, cislo+1):
       # for sloupec in range(0, cislo):
        print(" o "*radek, end="")
            
        print()
    pass

vstup = int(input("Zadej počet prvků pyramidy: "))
pyramida(vstup)
