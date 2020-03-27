"""
prvocisla.py

vyhodnotí, zda vložené číslo je prvočíslem

v druhá části spočítá prvních X prvočísel. číslo X zadá uživatel
"""

# test, zda číslo je prvočíslem
print()
print("Test, zda zadané číslo je prvočíslem")
cislo = int(input("Zadej celé kladné číslo > 1: "))

if cislo > 1:
    delitele = []
    for i in range(1, cislo+1):
        if cislo % i == 0:
            delitele.append(i)
    print(f"Dělitelé čísla {cislo} jsou: {delitele}")
    pocet = (len(delitele))

    if pocet > 2:
        print(f"Číslo {cislo} není prvočíslem. ")
    else:
        print(f"Číslo {cislo} je prvočíslem. ")
else:
    print()
    print("Zadané číslo není kladné celé číslo > 1.")


# vypsání prvočísel

limit = int(input("Zadej počet prvočísel, které chceš vypsat: "))

if limit > 0:
    seznamPrvocisla = []
    cislo = 2

    while len(seznamPrvocisla) < limit:

        delitele = []
        for i in range(1, cislo+1):
            if cislo % i == 0:
                delitele.append(i)

        pocet = (len(delitele))
        if pocet == 2:
            seznamPrvocisla.append(cislo)
        cislo += 1
print()
print(f"{limit} prvočísel je v intervalu 1 - {max(seznamPrvocisla)}.")
print("Seznam prvních ",limit," prvočísel je:\n", seznamPrvocisla)
