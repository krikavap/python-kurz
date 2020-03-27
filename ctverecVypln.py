"""
ctverecVypln.py
program, který na vstupu získá 
přirozené číslo a znak pro vykreslení, 
a na výstupu vykreslí čtverec, jehož 
strana bude obsahovat právě tolik znaků, 
jaká byla hodnota na vstupu.
Čtverec bude vykreslený s výplní.
"""

def vykresli(delka, vypln):
    for i in range(0, delka):
        print((vypln + " ") * delka)
    print()




strana = int(input("Zadej velikost strany čtverce: "))
znak = str(input("Zadej znak, kterým bude čtverec vykreslen a vyplněn: "))

vykresli(strana, znak)
