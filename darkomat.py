"""
darkomat.py
Blíží se Vánoce a každý ve firmě
přichystá pozornost pro jednoho kolegu.
Nesmí se stát, že by dával dárek sám sobě.
Vypisuj, kdo komu připraví dárek na vánoční
večírek.
Připrav si dva identické seznamy osob
ve firmě. Využívej příkaz pro smazání
položky ze seznamu.


"""

import random

lide = ["Petr", "Pavel", "Josef","František", "Jakub", "Qvído", "Jana", "Lenka", "Eliška", "Marie", "Šárka", "Andělka"]
kopie = lide.copy()
#print(len(lide))

for clovek in kopie:        # prochází všechny prvky v kopie
    #print("clovek:", clovek)
    proKoho = random.choice(lide)       # vybere z lidé
    #print("proKoho:", proKoho)
    if proKoho == clovek:               # pokud vybraný člověk z kopie je shodný z lidé
        proKoho = random.choice(lide)   # pak se generuje znovu
        #print("proKoho:", proKoho)
        #kopie.remove(proKoho)
    print(f"{clovek} připraví dárek {proKoho}")
    lide.remove(proKoho)            # již obdarovaný se vymaže ze seznamu lide
