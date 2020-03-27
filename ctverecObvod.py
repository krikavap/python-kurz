"""
ctverecObvod.py
Vytvoř program, který na vstupu získá 
přirozené číslo, a na výstupu hvězdičkami 
vykreslí obvod tohoto čtverce.
 
Př.:
vstup = 5
výstup:
 
* * * * *
*       *
*       *
*       *
* * * * *
 
"""
def vykresliObvod(delka):
    for i in range(0, delka):
        vnitrek = delka + (delka - 3)
        if (i == 0) or (i == delka - 1):
            print("* " * delka)
        else:
            print("*" + chr(32) * vnitrek + "*")
    print()
        

delka = int(input("Zadej délku strany čtverce: "))

vykresliObvod(delka)