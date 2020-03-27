"""
výpočet obvodu a obsahu kruhu

vstup: průměr kruhu
výstup: obvod a obsah kruhu

postup:
1) zadání parametru průměr
2) výpočet
3) vypsání výsledku na obrazovku

"""
prumer=float(input("Zadej průměr kruhu:"))

obvod=prumer*3.14
obsah=((prumer/2)**2)*3.14

print("Obvod kruhu je:",obvod,"cm")
print("Obsah kruhu je:",obsah,"cm2")