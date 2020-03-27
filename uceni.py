"""
uceni.py

načte uživatelovu odpověď (0=ne, 1=ano) na dotaz
odpověď programu dle vstupu
"""
#odpoved is None

odpoved = input("Učíš se nyní Python? Jako odpověď zadej 0 pro ne, 1 pro ano:")
if odpoved:                 # pokud existuje vstup z klávesnice (mimo enter)
    if odpoved =="1":
        print("Ano")
    elif odpoved == "0":
        print("Ne")
    else:
        print("Musíš zadat buď 0 nebo 1")
else:
    print("Nezadáno")   # pro případ, že např. jen odklepnu enter
