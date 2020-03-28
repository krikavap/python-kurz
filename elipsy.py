"""
elipsy.py

spočte obsah elipsy při znalosti hlavní (a) a vedlejší (b) poloosy
"""
import math

def obsahElipsy(hlavni, vedlejsi):
    obsah = math.pi * hlavni * vedlejsi
    return obsah

a = float(input("Zadej rozměr hlavní poloosy: ")) 
b = float(input("Zadej rozměr vedlejší poloosy: ")) 

obsah = obsahElipsy(a, b)
print(f"Obsah elipsy je: {obsah:7.3f}")