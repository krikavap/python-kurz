"""
mnohouhelnik.py

Vytvoř funkci, která bude vykreslovat mnohoúhelník. 
Uživatel na začátku zadá číslo > 2, program pak vykreslí 
patřičný mnohoúhelník (rovnostranný trojúhelník, čtverec, 
pětiúhelník atd.).


"""

import turtle

def mnohouhelnik(vrcholu, krok):
    uhel = 360 / vrcholu
    turtle.shape("turtle")
    turtle.pencolor("red")
    turtle.pensize(3)
    for i in range(vrcholu):
        turtle.forward(krok)
        turtle.left(uhel)
    turtle.done()


x = 0
krok = 0
while x < 3 or krok < 5:
    x = int(input("Zadej, počet vrcholů vykreslovaného mnohoúhelníka (minimálně 3): "))
    krok = int(input("Zadej délku strany (minimálně 5): "))

mnohouhelnik(x, krok)
