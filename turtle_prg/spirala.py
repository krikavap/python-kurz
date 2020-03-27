"""
spirala.py

Vytvoř program, který jedním tahem vykreslí spirálu n-úhelníku. 
N-úhelník musí být číslo > 2.
"""


import turtle
import random

def spirala(vrcholu, krok, posun):
    barva = ["red", "blue", "green", "purple", "yellow"]
    turtle.shape("turtle")
    turtle.pensize(3)
    
    uhel = 360 / vrcholu
    posun = 100/posun

    for j in range(5):
        for i in range(vrcholu):
            turtle.pencolor(random.choice(barva))
            turtle.forward(krok)
            turtle.left(uhel)
            krok = krok + posun
    turtle.done()


x = 0
krok = 0
while x < 3:
    x = int(input("Zadej, počet vrcholů vykreslovaného mnohoúhelníka (minimálně 3): "))

posun = 10
krok = 20
spirala(x, krok, posun)
