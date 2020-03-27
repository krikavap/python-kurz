"""
odstranCZ.py
Vytvoř funkci, která v řetězci na vstupu nahradí české znaky 
za znaky anglické abecedy.
Tuto funkci dále používej 
v šifrovacích programech, které následují, a to tak, že si buď: 
kód funkce zkopíruješ na začátek dalšího programu; 
nebo si na internetu zjistíš, jak vytvářet a importovat vlastní moduly. 
Opravdu to není těžké :)
"""

def zbavSeCZ(retezec):

    frm = "ěščřžýáíéĚŠČŘŽÝÁÍÉÚŮúůťďŤĎŇň"
    to = "escrzyaieESCRZYAIEUUuutdTDNn"
    trans_table = str.maketrans(frm, to)
    secret_code = retezec.translate(trans_table)
    #print(secret_code)   
    return secret_code


vstup = str(input("Zadej řetězec: "))
vystup = zbavSeCZ(vstup)
print(vystup)