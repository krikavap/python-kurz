"""
jazykC.py

různé způsoby formátování čísla pí

program v cyklu vypíše 0. až 10. mocninu čísla 10 zarovnanou vpravo
"""

import math

# formátování pí
pi = math.pi

print("bez formátování: pí = ",pi)
print("%f: pí = ","%f" % pi)
print("%.2f: pí = ","%.2f" % pi)
print("%10.2: pí = ","%10.2f" % pi)
print("%10.3: pí = ","%10.3f" % pi)
print("%10.4: pí = ","%10.4f" % pi)

# 0. až 10. mocninu čísla 10 zarovnanou vpravo
for i in range(0,11):
    mocnina = pow(10, i)
    print("%2i" %i,". mocnina 10 je:", "%12i" %mocnina)
    pass

print()

for i in range(0,11):
    mocnina = pow(10, i)
    print("%2i" %i,". mocnina 10 je:", "%012i" %mocnina)
    pass
