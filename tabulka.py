"""

tabulka.py

vytvoří tabulku o rozměrech x a y
naplní ji náhodnými znaky z A - Z

"""

import random

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

x = int(input("Zadej rozměr x: "))
y = int(input("Zadej rozměr y: "))

if (x > 0) and (y > 0):
    print()
    for i in range(0 , y):
        for j in range(0 , x):
            pismenko = random.choice(abc)
            print (pismenko, end=" ")
        print()
else:
    print("Oba zadané rozměry musí být větší než nula.")
