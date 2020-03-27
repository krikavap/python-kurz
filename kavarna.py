"""
kavarna.py

program vypíše nabídku kavárny - název nápoje, objem, cenu v tabulce

"""

napoj = "káva s mlékem", "džus", "capuccino", "voda","smetana"
objem = "200 ml", "250 ml","180 ml","500 ml","50 ml"
cena = "25", "30", "35", "15", "10"

pocet = len(napoj)

for i in range(0, pocet):
    print(f"{napoj[i]:>15}  {objem[i]:<6}  {cena[i]:>2} Kč ")
