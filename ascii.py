"""
ascii.py

vypíše znaky acsii 0-127
"""

for i in range(0,128):
    znak = chr(i)
    # print(f"{i:03} je {znak}", end = " ")
    print(f"{i:03}: {znak}\t", end = " ")
    pass
