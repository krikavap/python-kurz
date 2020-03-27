"""
absolutni.py


vypočte absolutní hodnotu čísla bez použití knihovny math
"""

cislo_zadane = float(input("Zadej libovolné číslo: "))

if cislo_zadane < 0:
    cislo = cislo_zadane * (-1)
else:
    cislo = cislo_zadane

print(f"Absolutní hodnota čísla {cislo_zadane} je {cislo}" )
