"""
smenarna.py

program vypočte výši poplatku při směně czk na eur.

poplatek je 1% ze směny, minimální poplatek je 50 Kč
"""

castka = int(input("Kolik Kč chceš vyměnit? "))

poplatek = castka * 0.01

if poplatek < 50:
    poplatek = 50

print(f"Poplatek za výměnu {castka} Kč je {poplatek:,.2f} Kč")
