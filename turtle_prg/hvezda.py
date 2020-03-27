"""
hvezda.py
Vytvoř funkci, která dle zadaného čísla vykreslí obrys hvězdy. 
Vstupem bude celé číslo > 2. Vytvoř funkci, která dle zadaného čísla vykreslí 
jednou čarou hvězdu. Vstupem bude celé číslo > 2.
"""

import turtle
import random

def hvezda(vrcholu, krok, posun):
    barva = ["red", "blue", "green", "purple", "yellow"]
    turtle.shape("turtle")
    turtle.pensize(3)
    
    uhel1 = 360 / vrcholu
    uhel2 = 360 *2 / vrcholu
    uhelTupy = uhel1 *2
    uhelOstry = uhel1 
    
    for i in range(vrcholu):
        turtle.pencolor(random.choice(barva))
        turtle.forward(krok)
        turtle.right(uhelTupy)
        turtle.forward(krok)
        turtle.left(uhelOstry)
        
    turtle.done()


x = 0
krok = 0
while x < 3:
    x = int(input("Zadej, počet cípů hvězdy (minimálně 3): "))

posun = 10
krok = 20
hvezda(x, krok, posun)
