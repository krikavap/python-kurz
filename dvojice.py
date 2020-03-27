"""
dvojice.py
Losuj dvojice dívek a chlapců do školních
lavic. Jména se nesmí opakovat (Maruška
nemůže sedět zároveň s Jeníkem a Péťou).
Měj dva stejně dlouhé seznamy,
v jednom dívky, ve druhém chlapce.
Seznamy náhodně zamíchej a vypiš dvojice
dívka–chlapec (vždy [0] index z jednoho
seznamu a k němu [0] index ze druhého atd.).
"""
import random

kluci = ["Petr", "Pavel", "Josef","František", "Jakub", "Qvído"]
holky = ["Jana", "Lenka", "Eliška", "Marie", "Šárka", "Andělka"]

random.shuffle(kluci)
random.shuffle(holky)

for i in range(0, len(kluci)):
    print(f"{i + 1}. dvojice je {kluci[i]} a {holky[i]}")
