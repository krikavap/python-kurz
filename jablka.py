"""
jablka.py
program rozdělí daný počet jablek mezi daný počet dětí.
jablka lze dávat pouze celá, nikoli jejich části

vstup=počet jablek, počet dětí (celá čísla)
výstup=počet jablek na jedno dítě, zbytek

postup:
1.načtení vstupů
2. výpočet
3. výstup výsledků na obrazovku

"""
jablka=int(input("počet jablek k rozdělení:"))
deti=int(input("počet dětí:"))

pocet_na_dite=jablka//deti
zbytek=jablka%deti

print("počet jablek na jedno dítě:",pocet_na_dite)
print("zbyde nerozdělených jablek:", zbytek)
