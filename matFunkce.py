"""
matFunkce.py

program načte vložené číslo a dle volby uživatele vypíše při stisku:
1-> druhou mocninu
2-> druhou odmocninu
3-> faktoriál

Zároveň ošetři vstup nekorektních hodnot z klávesnice
Použití switch -> case

"""

import math
cislo = int(input("Zadej libovolné celé kladné číslo:"))
odpoved = input("Stiskni 1-> pro druhou mocninu, 2-> pro druhou odmocninu 3-> pro faktoriál:")
if odpoved:                 # pokud existuje vstup z klávesnice (mimo enter)
    if odpoved =="1" or odpoved =="2" or odpoved == "3":
        if odpoved =="1":
            druhamocnina = cislo**2
            print(f"Druhá mocnina z {cislo} je {druhamocnina}")
        elif odpoved == "2":
            druhaodmocnina = cislo**(1/2)
            print(f"Druhá odmocnina z {cislo} je {druhaodmocnina:.5f}")
        else:
            faktorial = math.factorial(cislo)
            print(f"Faktoriál z {cislo} je {faktorial}")
    else:
        print("Musíš zadat buď 1 nebo 2 nebo 3")
else:
    print("Nezadáno")   # pro případ, že např. jen odklepnu enter
