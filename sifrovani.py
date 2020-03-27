"""
sifrovani.py
 
funkce „caesar“
Vytvoř funkci, která řetězec na vstupu zašifruje Caesarovou šifrou, 
tedy provede posun znaků o zadaný počet pozic vpravo. 
Pokud si chceš ušetřit práci, použij pouze znaky anglické abecedy.
Wikipedie: Princip Caesarovy šifry je založen na tom, že všechna písmena 
zprávy jsou během šifrování zaměněna za písmeno, které se abecedně nachází 
o pevně určený počet míst dále (tj. posun je pevně zvolen).
 
funkce „alberti“
Vytvoř funkci, která řetězec na vstupu zašifruje Albertiho šifrou.
Wikipedie: Původní Albertiho šifra (...) používala dvě šifrovací abecedy (...) 
Pokud bychom chtěli zašifrovat slovo „silnice“, postupovali bychom takto: 
první písmeno „s“ bychom zašifrovali podle první abecedy: S→L. 
Druhé písmeno bychom zašifrovali podle druhé abecedy: I→E. 
Třetí písmeno opět podle první abecedy: L→E. Pak N→J, I→B, C→Y a E→X. 
Výsledné šifrové slovo by bylo: „LEEJBYX“.
"""
import random

# nejprve se zbavíme češtiny

def zbavSeCZ(retezec):

    frm = "ěščřžýáíéĚŠČŘŽÝÁÍÉÚŮúůťďŤĎŇň"
    to = "escrzyaieESCRZYAIEUUuutdTDNn"
    trans_table = str.maketrans(frm, to)            # standardní metoda pro práci s řetězci - připraví transformační tabulku
    secret_code = retezec.translate(trans_table)    # standardní metoda pro práci s řetězci - provede transformaci dle transformační tabulky
    #print(secret_code)   
    return secret_code


def ceasar(retezec, posun, frm):
    """
    zašifruje řetězec ceasarovou šifrou: posune každý znak v abecedě o zadaný počet znaků
    parametry:
    retezec - řetězec, který má být zašifrován
    posun - kolik znaků má být posun v abecedě
    frm - šifrovací abeceda
    """
    to = frm[posun:] + frm[:posun]
    #print(frm)
    #print(to)
    trans_table = str.maketrans(frm, to)
    secret_code = retezec.translate(trans_table)
    #print(secret_code)   
    return secret_code

def deCeasar(retezec, posun, frm):
    """
    rozšifruje řetězec zašifrovaný ceasarovou šifrou: posune každý znak v abecedě o zadaný počet znaků
    parametry:
    retezec - řetězec, který má být rozšifrován
    posun - kolik znaků má být posun v abecedě
    frm - šifrovací abeceda
    """
    to = frm[posun:] + frm[:posun]
    trans_table = str.maketrans(to, frm)
    secret_code = retezec.translate(trans_table)
    return secret_code

def skupiny(retezec, x):
    """
    řetězec znaků zbaví všech mezer, a rozdělí do skupin po x písmenech
    """
    retezec = retezec.replace(" ","")
    delka = len(retezec)
    pocet = delka // x
    zbytek = delka % x
    novyRetezec = ""
    zacatek = 0
    konec = x
    for i in range(0, pocet):
        novyRetezec = novyRetezec + retezec[zacatek:konec] + " "
        zacatek = zacatek + x
        konec = zacatek + x
    novyRetezec = novyRetezec + retezec[zacatek : zacatek + zbytek]
    return novyRetezec

def alberti(retezec, frm, to1, to2):
    """
    zašifruje Albertiho šifrou
    frm - zdrojová abeceda
    lichá písmena dle abecedy to1
    sudá písmena dle abecedy to2
    vrátí zašifrovaný řetězec
    """
    novyRetezec = ""

    trans_table1 = str.maketrans(frm, to1)
    secret_code1 = retezec.translate(trans_table1)

    trans_table2 = str.maketrans(frm, to2)
    secret_code2 = retezec.translate(trans_table2)

    for i in range(0, len(retezec)):
        if i % 2 == 0:
            novyRetezec = novyRetezec + secret_code2[i]
        else:
            novyRetezec = novyRetezec + secret_code1[i]
        pass
    return novyRetezec

def deAlberti(retezec, frm, to1, to2):
    """
    dezašifruje Albertiho šifru
    frm - zdrojová abeceda
    lichá písmena dle abecedy to1
    sudá písmena dle abecedy to2
    vrátí rozšifrovaný řetězec
    """
    novyRetezec = ""

    trans_table1 = str.maketrans(to1, frm)
    secret_code1 = retezec.translate(trans_table1)

    trans_table2 = str.maketrans(to2, frm)
    secret_code2 = retezec.translate(trans_table2)

    for i in range(0, len(retezec)):
        if i % 2 == 0:
            novyRetezec = novyRetezec + secret_code2[i]
        else:
            novyRetezec = novyRetezec + secret_code1[i]
        pass
    return novyRetezec

def abeceda(abec):
    """
    náhodně promíchá řetězec abec a vrátí jej
    převod do typu list je nutný - metoda random.shuttle neumí pracovat s řetězcem, ale jen s listem
    """
    pole = []
    pole = list(abec)
    random.shuffle(pole)
    abec = "".join(pole)
    return abec


#abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
vstup = str(input("Zadej řetězec: "))
posun = int(input("Zadej posun znaků: "))
velikost = 0
while velikost <= 0:
    velikost = int(input("Zadej velikost skupiny znaků (větší než 0): "))
vystup = zbavSeCZ(vstup)
vystup = vystup.upper()
# print(vystup)

# část Ceasarova šifra
vystupCe = ceasar(vystup, posun, abc)
# print(vystupCe)
vystupCe = skupiny(vystupCe, velikost)
print()
print("Výstup: řetězec zašifrovaný Ceasarovo šifrou: ",vystupCe)
vystupCe = deCeasar (vystupCe, posun, abc)
print("Výstup: kontrolní dešifrování: ",vystupCe)

# část Albertiho šifra
# print(abc)
abeceda1 = abeceda(abc)
# print(abeceda1)

abeceda2 = abeceda(abc)
# print(abeceda2)

vystupAl = alberti(vystup, abc, abeceda1, abeceda2)
# print(vystupAl)

vystupAlSkupiny = skupiny(vystupAl, velikost)
print()
print("Výstup: řetězec zašifrovaný Albertiho šifrou: ",vystupAlSkupiny)

vystupAl = deAlberti(vystupAl, abc, abeceda1, abeceda2)
print("Výstup: kontrolní dešifrování: ", vystupAl)
