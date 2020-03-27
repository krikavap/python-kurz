"""
ctverec.py

na obrazovce vykreslí čtverec tvořený hvězdičkami
délka strany čtverce je zadána uživatelem

"""
delka = int(input("Zadej délku strany čtverce (celé číslo): "))

znak = "*"

if delka > 0:

    # horní strana
    print(f"\t{znak * delka}")

    # levá a pravá strana
    """
    i = 0
    while i in range(0, delka - 2):
        print(f"\t{znak}{chr(32) * (delka - 2)}{znak}")
        i = i + 1
    """
    for i in range(0, delka - 2):
        print(f"\t{znak}{chr(32) * (delka - 2)}{znak}")
        
    # spodní strana
    print(f"\t{znak * delka}")
else:
    print("Musíš zadat kladné číslo")
