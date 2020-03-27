"""
pocasi.py

program vyhodnotí zadanou teplotu v stupních C na škále mráz, chladno, příjemně, horko

"""
teplota = int(input("Zadej teplotu ve stupních C: "))

if teplota in range(15, 25):
    print ("Je příjemně")
else:
    if teplota in range(0,15):
        print("Je zima")
    elif teplota < 0:
        print("Mrzne")
    else:
        print("Je horko")
        pass
    pass
