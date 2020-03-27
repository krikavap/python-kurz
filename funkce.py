"""
funkce.py

Demonstruje dva druhy uživatelských funkcí:
tzv. čistá funkce, která vrací hodnotu - v ukázce funkce obvodCtverce()
a funkce, která hodnotu nevrací - v ukázce funkce obsahCtverce()
"""



def obvodCtverce(strana):
    """
    obvodCtverce()
    parametr: délka strany
    tzv. čistá funkce vracející hodnotu za klíčovým slovem return
    funkce obvodCtverce vypočte obvodCtverce
    parametr funkce je délka strany čtverce
    """
    obvod = 4 *  strana
    return obvod

def obsahCtverce(strana):
    """
    obsahCtverce()
    parametr: délka strany
    funkce nevrací hodnotu, ale tiskne výsledek

    """
    obsah = strana ** 2
    print("-" * 10)
    print(f"Obsah čtverce je {obsah}")
    print("-" * 10)


a = float(input("Zadej délku strany: "))

# tisk v hlavním programu
print("-" * 10)
print("Obvod čtverce je ",obvodCtverce(a))  # volání čisté funkce (funkce, která vrací hodnotu), argument a (délka strany)
print("-" * 10)

obsahCtverce(a)     # volání funkce, která nevrací hodnotu, ale tiskne výstupy z těla funkce
# print(obsahCtverce(a))

print(__doc__)     # vypíše komentáře (dokumentaci) daného programu mezi """ a """
print(obvodCtverce.__doc__)     # vypíše komentáře (dokumentaci) dané funkce mezi """ a """
print(obsahCtverce.__doc__)
