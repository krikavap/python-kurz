"""
nakupniSeznam.py

nejprve je zadáno počet položek nákupu
pak se zadávají položky seznamu a kontrolují se na duplicitu
seznam je vypsán před a po setřídění

"""
pocet = int(input("Zadej počet položek v seznamu: "))

i = 0
seznam = []
if pocet > 0:
    while i in range(0, pocet):
        j = i + 1
        polozka = str(input(f"Zadej {j}. položku v seznamu: "))
        polozka = polozka.lower()
        if polozka in seznam:
            print(f"Položka {polozka} již v seznamu existuje. Zadej jinou.")
            i = i - 1
            j = j - 1
        else:
            seznam.append(polozka)

        if j < pocet:
            print(f"Ještě ti zbývá zadat {pocet - j} položek seznamu.")
        elif pocet == j:
            print(f"Zadal jsi poslední položku seznamu.")
        i = i + 1
    print()
    print(seznam)
    seznam.sort()
    print(seznam)
else:
    print("Nebyl zadán kladný počet položek nákupního seznamu.")
