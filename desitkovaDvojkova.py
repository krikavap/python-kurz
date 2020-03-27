"""
desitkovaDvojkova.py

"""

cislo = int(input("Zadej celé číslo v desítkové soustavě: "))
x = cislo

seznam = []

while x != 0:

    zbytek = x % 2
    seznam.append(zbytek)

    x = x // 2
    #print (x)

zacatek = 0
konec = len(seznam)

vysledek = []
dvojkove = ""

for i in range (konec-1, zacatek-1, -1):
    vysledek.append(str(seznam[i]))

dvojkove = "".join(vysledek)
dvojkove = "0" * (8 - len(dvojkove)) + dvojkove

print ()
print (f"{cislo} v desítkové soustavě je {dvojkove} ve dvojkové soustavě")


"""
a opačně dvojková na desítkovou
"""

dvojkove = str(input("Zadej celé číslo ve dvojkové soustavě: "))
cislo = 0
seznam = list(dvojkove)
zacatek = 0
konec = len (seznam)

for i in range(zacatek, konec):
    cislo = cislo + int(seznam[i])*2**(konec - i - 1)
    #print (f"i={i}, konec - i - 1 ={konec-i-1}, cislo = {cislo}")
print()
print (f"{dvojkove} ve dvojkové soustavě je {cislo} v desítkové soustavě")
