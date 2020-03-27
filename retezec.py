"""
retezec.py

uloží řetězec, zjistí jeho délku, vypíše první a poslední znak

pomocí cyklu vypíše celý řetězec pod sebou

"""

retezec = str(input("Napiš libovolný řetězec znaků: "))

delka = len(retezec)

print()
print(f"Délka řetězce \"{retezec}\" je {delka} znaků.")
print(f"První znak řetězce \"{retezec}\" je znak \"{retezec[0]}\"")
print(f"Poslední znak řetězce \"{retezec}\" je znak \"{retezec[delka-1]}\"")

print()
for i in range(0, delka):
    print(f" {retezec[i]}")
