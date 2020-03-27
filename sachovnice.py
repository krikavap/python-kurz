"""
sachovnice.py

program, který vykreslí šachovnici
# 8 × 8 znaků naplněnou střídavě znaky B a W
(jako black a white).
"""

odpoved = ""


def sachovnice():
    i = 0
    for i in range(0, 9):
        for j in range(0, 8):
            if j % 2 == 0:
                print(" B ", end="")
            else:
                print(" W ", end="")
        print()
odpoved = str(input("Chceš vykreslit šachovnici? (A pro ano, N pro ne)"))
odpoved = odpoved.lower()

while odpoved == "a":
    sachovnice()
    print()
    odpoved = str(input("Chceš vykreslit šachovnici? (A pro ano, N pro ne)"))
    odpoved = odpoved.lower()

