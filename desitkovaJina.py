"""
desitkovaJina.py

zobecnění programu desitkovaDvojkova.py

umožňuje zvolit, na jakou soustavu se má převádět

implementována je dvojková - devítková a hexa

"""


cislo = int(input("Zadej celé číslo v desítkové soustavě: "))
x = cislo
soustava = 0


while (soustava not in range(2, 10)) and (soustava !=16):
    soustava = int(input("Zadej, do jaké soustavy převádíme (2 pro dvojkovou, 3 pro trojkovou ... 9 pro devítkovou, 16 pro hexa): "))

seznam = []

while x != 0:

    zbytek = x % soustava
    seznam.append(zbytek)

    x = x // soustava
    #print (x)

zacatek = 0
konec = len(seznam)

if soustava == 16:
    for i in range(0, konec):

        if seznam[i]==10:
            seznam[i] = "A"
        elif seznam[i]==11:
            seznam[i] = "B"
        elif seznam[i]==12:
            seznam[i] = "C"
        elif seznam[i]==13:
            seznam[i] = "D"
        elif seznam[i]==14:
            seznam[i] = "E"
        elif seznam[i]==15:
            seznam[i] = "F"

vysledek = []
jinaSoustava = ""

for i in range (konec-1, zacatek-1, -1):
    vysledek.append(str(seznam[i]))

jinaSoustava = "".join(vysledek)
if soustava == 2:
    jinaSoustava = "0" * (8 - len(jinaSoustava)) + jinaSoustava

print ()
print (f"{cislo} v desítkové soustavě je {jinaSoustava} ve {soustava}-vé soustavě")


"""
a opačně dvojková na desítkovou
"""

jinaSoustava = str(input(f"Zadej celé číslo ve {soustava}-vé soustavě: "))
jinaSoustava = jinaSoustava.upper()
cislo = 0
seznam = list(jinaSoustava)
zacatek = 0
konec = len (seznam)


for i in range(zacatek, konec):
    if soustava == 16:
        if seznam[i]=="A":
            seznam[i] = 10
        elif seznam[i]=="B":
            seznam[i] = 11
        elif seznam[i]=="C":
            seznam[i] = 12
        elif seznam[i]=="D":
            seznam[i] = 13
        elif seznam[i]=="E":
            seznam[i] = 14
        elif seznam[i]=="F":
            seznam[i] = 15
    cislo = cislo + int(seznam[i])*soustava**(konec - i - 1)
    #print (f"i={i}, konec - i - 1 ={konec-i-1}, cislo = {cislo}")
print()
print (f"{jinaSoustava} ve {soustava}-vé soustavě je {cislo} v desítkové soustavě")
