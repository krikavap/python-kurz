"""
hexadec.py

program v cyklu vypíše 0. až 15. hodnotu hexadecimální číselné soustavy


"""
for i in range(0,16):
    print("%2x" % i)       #vypisuje pod sebou hexa s malými písmeny
    pass

for i in range(0,16):
    print("%02X" % i, end = " ")    #vypisuje vedle sebe hexa s velkými písmeny
    pass


"""
for i in range(0,16):
    print("%02X" % i)       #vypisuje vedle sebe hexa s velkými písmeny
    pass
"""
