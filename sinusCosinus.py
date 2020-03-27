"""
sinusCosinus.py

finkce sinus a cosinus pro hodnoty úhlu ve stupních

vstup: úhel ve stupních
výstup: sinus a cosinus

využití knihovny math
"""
import math

uhel=float(input("zadej úhel ve stupních:"))

#trigonometrické funkce pracují s úhly v radiánech
uhel=math.radians(uhel)
print("úhel v radiánech:", uhel)

sinus=math.sin(uhel)
cosinus=math.cos(uhel)

print("sinus:", sinus,"\n", "cosinus", cosinus)
