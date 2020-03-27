"""
znamka.py

program vyhodnotí zadané číslo, zda se jedná / nejedná o školní známku

"""
znamka = int(input("Zadej celé číslo: "))

if (znamka > 0) and (znamka <= 5):
    print (f"Číslo {znamka} je školní známkou")
else:
    print (f"Číslo {znamka} není školní známka")
    pass
