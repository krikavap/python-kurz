"""
bingo.py

hrací pole 5 x 5
naplnit čísly ze skupin 1-15, 16-30, 31-45, 46-60, 61-75

při losování počítač vylosuje 25 čísel z intervalu 1-75

vyhodnocení počtu shodných čísel

postup:
- vygenerovat 5 seznamů o 5 číslech ze skupin 1-15, 16-30, 31-45, 46-60, 61-75 (radek0 - radek5)
- vypsat hrací pole
- seznamy spojit do jednoho (vsazenaCisla)
- vygenerovat tažená čísla z intervalu 1-75 a nasypat je do pole tazenaCisla
- porovnat pole vsazenaCisla a tazenaCisla a vypsat shodná čísla a jejich počet
"""

import random
import os

def clear():
    os.system("cls")
    return

cisla = []
pomCisla = []
vsazenaCisla = []
tazenaCisla = []
omezeni = []
shodnaCisla = []

# vsazenaCisla priprava
for i in range(1, 77, 15):      # pole s hodnotami zacatek a konec intervalu
    omezeni.append(i)

for j in range(0, len(omezeni) - 1):    # cyklus pro přípravu vsazených čísel
    zacatek = omezeni[j]
    konec = omezeni[j + 1]

    pomCisla = []
    for i in range(zacatek, konec):         # generování skupin čísel
        pomCisla.append(i)
    vsazenaCisla.extend(random.sample(pomCisla, 5))     # generování náhodných čísel z připravených skupin
    vsazenaCisla.sort()
clear()
print("Vsazená čísla jsou: ", vsazenaCisla)

# tah cisel
pomCisla = []
for i in range(1, 76):      # generování řady
    pomCisla.append(i)

tazenaCisla.extend(random.sample(pomCisla, 25))     # losování 25 náhodných čísel z vygenerované řady
tazenaCisla.sort()
print("Tažená čísla jsou: ",tazenaCisla)

# porovnání vsazenaCisla a tazenaCisla
for i in range(0, 25):
    for j in range(0,25):
        if tazenaCisla[i] == vsazenaCisla[j]:
            shodnaCisla.append(tazenaCisla[i])

print("-"*20)
print("Uhodl jsi ", len(shodnaCisla), "čísel.")
print(f"To je úspěšnost {len(shodnaCisla)/25*100:7.3f} %")
print("Jsou to tato čísla: ", shodnaCisla)
print("-"*20)
