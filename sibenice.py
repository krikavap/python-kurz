"""
sibenice.py

v proměnné klic je tajný klíč
pomocná proměnná pom je naplněna *
uživatel bude zadávat písmena a pokud uhodne, přepíše hvězdičku na písmeno

"""
import time
import os

def clear():
    os.system("cls")
    return

"""
sib = [
    "       \n      \n      \n      \n      \n_________",
    "       \n      \n      \n      \n  |   \n_________",
    "       \n      \n      \n  |   \n  |   \n_________",
    "       \n      \n  |   \n  |   \n  |   \n_________",
    "       \n  |   \n  |   \n  |   \n  |   \n_________",
    " _     \n  |   \n  |   \n  |   \n  |   \n_________",
    " __    \n  |   \n  |   \n  |   \n  |   \n_________",
    " ___   \n  |   \n  |   \n  |   \n  |   \n_________",
    " ____  \n  |   \n  |   \n  |   \n  |   \n_________",
    " ____  \n  |   \n  |   \n  |   \n  |   \n_________",
    " ____  \n  |   \n  |   \n  |   \n  |   \n_________",
]
"""
sib = ["?",chr(2),chr(2)*2,chr(2)*3,chr(2)*4,chr(2)*5,chr(2)*6,chr(2)*7,chr(2)*8,chr(2)*9,chr(2)*10]

slovo = "TAJEMSTVÍ"
delka = len(slovo)
chyby = 0
pozice = 0
sifra = "*" * delka

clear ()
while (sifra != slovo) and (chyby < len(sib)):               # dokud není celé slovo uhodnuté a počet chyb není větší než řádky šibenice

    print ()
    print ("------------")
    print ("Hádej slovo: ")
    print ("------------")
    print ()
    print (sifra)

    for prvek in sib:               # procházej sib po prvcích

        if pozice > chyby:      # pokud pozice prvku v listu je větší než počet chyb, již nevykresluj řádek
            continue
        print (prvek)
        pozice = pozice + 1

    znak = str(input("Zadej písmeno: "))    # zadej znak
    znak = znak.upper()
    sifra = list(sifra)             # převod na list

    # je znak ve slovo?
    if znak in slovo:               # pokud je znak ve slově, dopln jej do sifra
        for i in range(0, delka):   # procházej cyklus 0 - délka slova
            if slovo[i] == znak:    # najdeš-li ve slově zadaný znak
                sifra[i] = znak     # v listu šifra přiřaď znak na pozici i
        clear()
    else:
        chyby = chyby + 1
        if chyby == len(sib):
            print (f"To ti fakt nevyšlo... {chyby} chyb. Visíš...")
        else:

            clear()

    pozice = 0
    sifra = "".join(sifra)              # převedení šifry z listu do řetězce
    #clear()
    if sifra == slovo:

        print ()
        print (f"Výborně, uhodl jsi tajné slovo {slovo} !!!")
        print (f"Dokázal jsi to s {chyby} chybnými odpověďmi ...")
