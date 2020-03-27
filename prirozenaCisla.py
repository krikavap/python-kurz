"""
prirozenaCisla.py

program vypíše z kolika jednotek, desítek,
stovek a tisíců se skládá číslo na vstupu

vstup: přirozené číslo
výstup: počet jednotek, desítek, stovek, tisíců

postup:
1. načtení vstupní hodnoty
2. výpočty (celočíselné dělení)
3. průběžné výstupy
"""

cislo_puvodni = int(input("zadej přirozené číslo: "))
cislo = cislo_puvodni


tisice = cislo//1000
cislo = cislo%1000

stovky = cislo//100
cislo = cislo%100

desitky = cislo//10
cislo = cislo%10

jednotky = cislo//1
cislo = cislo%1


print("tisíce:", tisice)
print("stovky:", stovky)
print("desítky:", desitky)
print("jednotky:", jednotky)
print("zadané číslo:", cislo_puvodni)


"""
dvojková soustava

"""
cislo_bin = bin(cislo_puvodni)[2:]
print("dvojkové vyjádření:", cislo_bin)
print(int(cislo_bin,2)) #zpětný převod na desítkovou soustavu

"""
šestnáctková soustava
"""
cislo_hex = hex(cislo_puvodni)[2:]
print("šestnáctková soustava:", cislo_hex)
print(int(cislo_hex,16))    #zpětný převod na desítkovou soustavu

"""
osmičková soustava
"""
cislo_oct = oct(cislo_puvodni)[2:]
print("osmičková soustava:", cislo_oct)
print(int(cislo_oct,8)) #zpětný převod na desítkovou soustavu
