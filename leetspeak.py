"""
leetspeak.py

zašifruje řetězec řečí L3375P34K

"""
retezec = str(input("Zadej: "))
znaky = "ABCEGIKLOSTYZ"
leet =  "48(361XL057J2"

retezec = retezec.upper()   # na velká písmena
seznam = list(retezec)      # převod do listu seznam
print (retezec)

for i in range(0, len(seznam)):     # projde celý list seznam (všechny prvky)
    if seznam[i] in znaky:          # pokud je prvek v seznamu také v klíči znaky, pak se zjistí jeho index
        index = znaky.find(seznam[i])
        seznam[i] = leet[index]         # prvek listu seznam je naplněn prvkem z leet na stejné pozici

retezec = "".join(seznam)           # převede list na string
print(retezec)
