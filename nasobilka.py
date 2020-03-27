"""
nasobilka.py

vypíše malou násobilku čísel 1 - 10 do přehledné tabulky

"""

for y in range (1, 11):
    for x in range (1, 11):

        print(f"{x:>2} * {y:>2} = {x*y:>3}")

    print("*"*30)


# vypsání jen výsledků násobení
print("*"*50)
for y in range (1, 11):
    for x in range (1, 11):
        print(f"{x*y:>4}", end ="")
    print()

print("*"*50)
