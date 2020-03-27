"""
prevody.py

program převede hodnutu zadanou v m na dm, cm, mm, km
čísla budou vypsána v exponenciálním tvaru

"""
cislo = int(input("Zadej hodnotu v celých metrech: "))

dm = cislo*10
cm = cislo*100
mm = cislo*1000
km = cislo/1000

print(f"{cislo} m je {km:.3e} km, {dm:.3e} dm, {cm:.3e} cm, {mm:.3e} mm")
