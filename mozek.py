"""
mozek.py

program ze zásoby slov vybere vždy jedno, přehází náhodně v něm písmena na vnitřních pozicích
slovo vypíše a vyzve uživatele, aby zapsal slovo správně

vyhodnocuje se počet správných odpovědí

vstup:
    databáze slov
    odpověď uživatele

výstup:
    porovnání odpovědi se s původním slovem

"""
import random

uroven_obtiznosti = 0
while uroven_obtiznosti not in range(1 , 3):
    uroven_obtiznosti = int(input("Zvol úroveň obtížnosti hry (stiskni 1 pro lehčí, 2 pro těžší): "))
    if uroven_obtiznosti == 1:
        dolni = 3
        horni = 6
        print("Zvolil jsi lehčí úroveň")
    else:
        dolni = 5
        horni = 15
        print("Dobře ty, zvolil jsi těžší úroveň")

# načtení db slov do seznamu
soubor = open("seznam_slov.txt", encoding = "utf-8")
obsah = soubor.read()
soubor.close()

# vyčištění obsahu (nahrazení teček čárkami)
seznam = []
seznam = obsah.split(sep=" ")    # načtení řetězce s oddělovači do seznamu (seznam = list)

def zamichejSlovo(slovo):               # slovo je type list
    hadejSlovo = []
    hadejSlovo.append(slovo[0])                 # první znak slova
    prostredek = slovo[1 : len(slovo) - 1]      # vybere prostředek slova a taky je list
    random.shuffle(prostredek)                  # zamíchá písmena

    hadejSlovo.extend(prostredek)               # rozsiri seznam o prvky prostredku - spojení dvou seznamů

    hadejSlovo.append(slovo[len(slovo) - 1])    # append přidá jeden prvek na konec listu

    return hadejSlovo

spravne = 0
odpovedi_celkem = 0
odpoved = ""
# cyklus while dokud uživatel bude chtít testovat dokud nedá 0.
while odpoved != "0":
    # výběr náhodného slova. random.choice vybere jeden prvek ze seznamu a převede jej na řetězec
    slovo = random.choice(seznam)
    delka_slova = len(slovo)

    if delka_slova in range(dolni, horni):
        slovo = list(slovo)
        hadejSlovo = zamichejSlovo(slovo)   # volání funkce, která zamíchá písmena

        while slovo == hadejSlovo:          # pokud náhodou zamíchané slovo je stejné jako původní, volá se fce znovu
            hadejSlovo = zamichejSlovo(slovo)

        hadejSlovo = "".join(hadejSlovo)    # převede seznam na řetězec
        slovo = "".join(slovo)              # převede seznam na řetězec

        print()
        print(f"Odpověz na otázku, o jaké slovo se jedná? Nebo stiskni 0 pro ukončení hry. ")
        print("-" * delka_slova)
        #print(slovo)
        print(hadejSlovo)
        print("-" * delka_slova)
        odpoved = str(input())
        print("-" * delka_slova)

        if odpoved == slovo:        # vyhodnocení správnosti odpovědi
            spravne = spravne + 1
            odpovedi_celkem = odpovedi_celkem + 1
            print("Správná odpověď")
        elif odpoved == "0":
            print("*" * 7)
            print("Končíme")
            if odpovedi_celkem > 0:
                print(f"Na {odpovedi_celkem} otázek jsi odpověděl {spravne} x správně, což je úspěšnost {100 * (spravne / odpovedi_celkem):5.2f}% ")
            print("*" * 7)
        else:
            odpovedi_celkem = odpovedi_celkem + 1
            print("Nesprávná odpověď")
            print(f"Správná odpověď byla {slovo}")
