"""
automat.py

program simuluje hrací automat
ze sady znaků ♥♦♣♠ vygeneruje náhodně 3 znaky.
Pokud jsou shodné, přičtou se body.
po výpisu bodů se program zeptá, zda pokračovat nebo ne. Pokud ne, vypíší se body a statistika.

fake code
fake = "♦"*3
vysledek = list(fake)

"""
import random
import os

def clear():
    os.system("cls")
    return


seznam = ["♥","♦","♣","♠"]

body = 0
pokracovat = True
celkem = 0
shoda = False
celkemZaHru = 0

while pokracovat:

    while not shoda:
        clear()
        vysledek = []

        for i in range(0, 3):
            vysledek.append(random.choice(seznam))
        print()
        print(vysledek)

        if vysledek[0] == vysledek[1] == vysledek[2]:
                body = body + 1
                shoda = True
                print("-" * 10)
                print(f"SHODA - TRALALÁ - ZÍSKAL JSI BOD.")
                print(f"K získání bodu jsi potřeboval {celkem} pokusů.")
                print(f"Tvoje úspěšnost v tomto kole je {(1 / celkem)*100:7.3f} %")
                print(f"Celkový počet bodů: {body}")
                print("-" * 10)
                print()
                celkem = 0

        dalsi = str(input("Pokračovat? (a/n)"))
        dalsi = dalsi.upper()

        if dalsi == "N":
            pokracovat = False
            shoda = True
        elif dalsi == "A":
            pokracovat = True
            shoda = False
            celkem = celkem + 1
            celkemZaHru = celkemZaHru + 1

print("-" * 10)
print(f"CELKOVÉ STATISTIKY:")
print(f"Celkový počet bodů: {body}")
print(f"K získání bodů jsi potřeboval {celkemZaHru} pokusů.")
print(f"Tvoje úspěšnost je {(1 / celkemZaHru)*100:7.3f} %")
print("-" * 10)
