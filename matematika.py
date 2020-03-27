"""
matematika.py

práce s knihovnou math

zaokrouhlování a mocniny
round, ceil, floor, pow, sqrt

"""
import math
#import random #modul pro generování náhodných čísel


#cislo=math.pi
cislo=float(input("Zadej číslo:"))
#cislo2=float(random.random())
mocnina=float(input("Zadej mocninu:"))

print(cislo)
print("funkce round", round(cislo,3)) #round - matematické zaokrouhlování
print("funkce ceil", math.ceil(cislo)) #ceil - zaokrouhlí na celé číslo nahoru
print("funkce floor", math.floor(cislo)) #floor - zaokrouhlí na celé číslo dolů
print("cislo:",cislo,"\n","mocnina:",mocnina)

cislo2=pow(cislo,mocnina)   #pow - umocňování
print("funkce pow(umocňování)", cislo2)
print("funkce sqrt(druhá odmocnina z proměnné cislo)", math.sqrt(cislo))    #sqrt - druhá odmocnina
print("odmocnina:", cislo2**(1/mocnina))    #pomocí ** a převrácené hodnoty mocniny lze libovolně odmocňovat
