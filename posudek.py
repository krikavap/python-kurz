"""
posudek.py

program ověří, zda lze dvě celočíselné hodnoty dělit beze zbytku

vstup: dvě celočíselné hodnoty
výstup: výrok o tom, zda lze dělit beze zbytku nebo ne

"""
hodnota1 = int(input("Zadej hodnotu dělence: "))
hodnota2 = int(input("Zadej hodnotu dělitele: "))

if hodnota2 != 0:
    zbytek = hodnota1 % hodnota2
    if zbytek > 0:
        print(f"{hodnota1} a {hodnota2} není dělitelná beze zbytku")
    else:
        print(f"{hodnota1} a {hodnota2} je dělitelná beze zbytku")
else:
    print("Nulovým dělitelem nelze dělit")
