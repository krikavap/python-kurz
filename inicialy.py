"""
inicialy.py

do jedné proměnné načte celé jméno osoby
vypíše iniciály
vypíše jméno a příjmení malými písmeny a následně velkými písmeny

načte věk uživatele jako řetězec
pokud bude obsahovat číslice, převede jej na integer, pokud ne, vypíše chybovou zprávu
věk vypíše na monitor spolu s datovým typem

vyzkouší metody center(), ljust(), zfill(), rjust()

"""
cele_jmeno = str(input("Napiš jméno a příjmení: "))
cele_jmeno = cele_jmeno.title()
jmeno, prijmeni = cele_jmeno.split(" ")

inicialy = jmeno[0]+prijmeni[0]
print(f"Iniciály jména {cele_jmeno} jsou: {inicialy.upper()}")

mcenter = cele_jmeno.center(50,"-")
mljust = cele_jmeno.ljust(50, "-")
mzfill = cele_jmeno.zfill(50)
mrjust = cele_jmeno.rjust(50,"-")

print(f"Demonstrace metody .center \"{mcenter}\"")
print(f"Demonstrace metody .ljust \"{mljust}\"")
print(f"Demonstrace metody .zfill \"{mzfill}\"")
print(f"Demonstrace metody .rjust \"{mrjust}\"")

vek = str(input("Kolik je mu let? "))

if vek.isnumeric():
    vek_int = int(vek)
    print(f"Věk je {vek_int}, datový typ je {type(vek_int)}")
else:
    print(f"Zadaný věk \"{vek}\" neobsahuje pouze číslice")
