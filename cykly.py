"""
cykly.py

s použitím cyklů for a while vypíše vzestupnou řadu celých čísel v rozsahu a až b
krajní hodnoty budou načteny ze vstupu od uživatele

vstupní čísla budou programem seřazena vzestupně.
vyhodnotí počet sudých a lichých čísel v intervalu a průměr všech čísel z intervalu


"""

a = int(input("Zadej jednu hranici intervalu: "))
b = int(input("Zadej druhou hranici intervalu: "))

if a > b:
    pom = a
    a = b
    b = pom

pocet_celkem = 0
pocet_sudych = 0
pocet_lichych = 0
soucet = 0

for i in range(a, b + 1):
    print(f"{i}\t", end = "")
    pocet_celkem = pocet_celkem + 1
    soucet = soucet + i
    if (i % 2) == 0:
        pocet_sudych = pocet_sudych + 1
    else:
        pocet_lichych = pocet_lichych + 1

prumer = soucet / pocet_celkem
print()
print(f"Celkem je v intervalu {a} až {b} {pocet_celkem} čísel.")
print(f"V intervalu je {pocet_sudych} sudých čísel a {pocet_lichych} lichých čísel")
print(f"Součet všech čísel v intervalu je {soucet} a jejich průměr je {prumer}. ")
