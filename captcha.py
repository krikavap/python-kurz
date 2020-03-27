"""
captcha.py

vygeneruje x náhodných pětimístných captcha kódů ze znaků a-z, A-Z,0-9
uloží je do seznamu
v cyklu se vypisují na monitor a požaduje se, aby je uživatel opsal
počítá se úspěšnost opisu

"""
import random

retezec = ""
pocet = 5
delka = 5
captcha = ""
seznam_captcha = []
uspesne = 0

# naplnění řetězce
for i in range(48, 58):
    retezec = retezec + chr(i)
for i in range(65, 91):
    retezec = retezec + chr(i)
for i in range(97, 123):
    retezec = retezec + chr(i)

print()
for i in range(0, pocet):
    for j in range(0, delka):
        pismenko = random.choice(retezec)
        captcha = captcha + pismenko

    vstup = str(input(f"Opiš řetězec \"{captcha}\": "))

    if vstup == captcha:
        uspesne = uspesne + 1
    else:
        print("Špatně opsáno. ")
    captcha = ""

uspesnost = uspesne / pocet * 100
print()
print(f"Úspešnost máš {uspesnost:6.2f}%")
