"""
prevodyGB.py

převádí GB na MB, kB, B, KiB, MiB, GiB
vstup je GB
"""

gb = int(input("Zadej hodnotu GB (celé číslo): "))

b = gb * 10 ** 9

kb = b / 1000
kib = kb * 1024/1000

mb = kb / 1000
mib = mb *(1024**2)/(1000**2)

gib = gb *(1024**3)/(1000**3)

print(f"{gb:>30,.4f} GB (Gigabajt)")
print(f"{mb:>30,.4f} MB (Megabajt)")
print(f"{kb:>30,.4f} kB (Kilobajt)")
print(f"{b:>30,.4f} B (bajt)")

print()

print(f"{gib:>30,.4f} GiB (Gibibajt)")
print(f"{mib:>30,.4f} MiB (Mebibajt)")
print(f"{kib:>30,.4f} KiB (Kibibajt)")

# bajtů

kib = 2 ** 10
mib = 2 ** 20
gib = 2 ** 30
tib = 2 ** 40

print()
print()
print(f" 1 Kibibajt = {kib:,} Bajtů")
print(f" 1 Mebibajt = {mib:,} Bajtů")
print(f" 1 Gibibajt = {gib:,} Bajtů")
print(f" 1 Tebibajt = {tib:,} Bajtů")
