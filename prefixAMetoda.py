"""
prefixAMetoda.py

různé možnosti formátování hodnoty s predixem f / metodou format.
proměnné pro text, celé a desetinné číslo, logická hodnota

"""

import math

pi = math.pi
text = "Ahoj"
cislo = 123

print("{} {} {}".format(pi, text, cislo))
print("{2} {0} {1}".format(pi, text, cislo))
print("{2} {0:.3f} {1}".format(pi, text, cislo))

print(f"{text}, {pi:.3f}, {cislo}")


# zarovnání doprava
for i in range(1,12):
    print(f"{i:>05}")
    pass


for i in range(1,12):
    print(f"{i:>2}", end=" ")
    pass

for i in range(1,15):
    vystup = pi**i
    print(f"{vystup:>16.5f}")
    pass
