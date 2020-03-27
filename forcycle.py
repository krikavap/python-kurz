"""
forcycle.py

"""
import os
def clear():
    os.system("cls")
    return

sib = [chr(2), "c", "b", "d", "e"]

slovo = "m"
znak = ""
chyby = 0
pozice = 0
clear ()

while (slovo!=znak) and (chyby < len(sib)):

    print("hlavička a zadání")
    for prvek in sib:

        if pozice > chyby:      # pokud pozice prvku v listu je větší než počet chyb, již nevykresluj řádek
            continue
        print("prvek sib",prvek)
        pozice = pozice + 1

    znak = str(input("Zadej znak: "))
    if slovo != znak:
        pozice = 0
        chyby = chyby + 1
        if chyby == len(sib):
            print ("Visíš")
        else:
            clear()
    else:
        print("bingo")
