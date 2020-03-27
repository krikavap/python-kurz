"""
tombola.py
K cenám tomboly losuj jméno osoby,
která cenu vyhrává.
Měj dva seznamy: ceny tomboly
(postupně procházej ceny od poslední
po první) a seznam osob. K ceně tomboly
náhodně vybírej ze seznamu osob.
"""
import random

osoby = ["Petr", "Pavel", "Josef","František", "Jakub", "Qvído", "Jana", "Lenka", "Eliška", "Marie", "Šárka", "Andělka"]
tombola = ["salám", "rum", "skleničky", "klobouk", "sekačku" ]
vyherci = random.sample(osoby, len(tombola))        # definujeme zde, aby mohl vyhrát jen jednu cenu

j = 0

for i in tombola:
    print(f"{i.capitalize()} vyhrává {vyherci[j]}.")
    j = j + 1
