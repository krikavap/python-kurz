"""
pozpatku.py

program načte řetězec (nebo i větu), rozseká jej a vypíše pozpátku


"""
retezec = str(input("Zadej slovo: "))

seznam = list(retezec)
pom = []
retezec_pozpatku = ""
zacatek = 0
delka = len(seznam)

for i in range(delka -1 , zacatek-1, -1):
    pom.append(seznam[i])
    print (seznam[i])
retezec_pozpatku = "".join(pom)
print (retezec_pozpatku)
