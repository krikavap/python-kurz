"""
nakup.py

program načte názvy zboží, jejich cenu a nakoupené množství a vypíše do tabulky
"""

zbozi = "mléko", "brambory", "pivo"
cena = "15", "30", "12"
mnozstvi = "2", "1.5", "3"

pocet = len(zbozi)

for i in range(0,pocet):

    print(f"{zbozi[i]:>10}\t {mnozstvi[i]:>3} * {float(cena[i]):>5.2f} = {(float(mnozstvi[i])*float(cena[i])):>5.2f} Kč" )
    pass
