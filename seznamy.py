"""
seznamy.py
"""
prvek_x = "X"

seznam = []
seznam.append("prvni")
seznam.append("druhý")
seznam.append(3)
seznam.append(prvek_x)
seznam.insert(3, 4)
print(seznam)

seznam.remove(3)
seznam.remove(4)
print (seznam)

seznam.extend(["pátá","buřty","okurky"])
print(seznam)

seznam.sort()
print(seznam)

retezec = "adfjlja"
print("tiskne jednotlivé znaky řetězce pod sebou")
for pismenko in retezec:    # tiskne jednotlivé znaky řetězce pod sebou
    print(pismenko)

seznam = list(retezec)  # list převede jednotlivé znaky proměnné na prvky seznamu
print(seznam)

seznam.sort()
print(seznam)

seznam.pop(1)   # smaže prvek seznamu na určené pozici
print(seznam)

print("první prvek seznamu ", seznam[1])

for prvek in seznam:
    print(prvek)

obsah = "jablko,hruska,svestka,hrozno,paprika"
seznam = obsah.split(sep=",")    # načtení řetězce s oddělovači do seznamu (seznam = list) - ideální pro parsování souboru txt
seznam.sort()
print(obsah)
print(seznam)
