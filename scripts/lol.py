import math

# Funkce pro výpočet plochy kruhu
def plocha_kruhu(polomer):
    if polomer <= 0:
        raise ValueError("Poloměr musí být kladné číslo.")
    plocha = math.pi * polomer ** 2
    kroky = "Výpočet plochy kruhu s poloměrem {}: \n".format(polomer) + \
            "Plocha = pi * poloměr ** 2 = {} * {} ** 2 = {}".format(math.pi, polomer, plocha)
    return plocha, kroky

# Funkce pro výpočet plochy obdélníku
def plocha_obdelnika(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Strany obdélníka musí být kladná čísla.")
    plocha = a * b
    kroky = "Výpočet plochy obdélníka s délkou stran {} a {}: \n".format(a, b) + \
            "Plocha = délka strany a * délka strany b = {} * {} = {}".format(a, b, plocha)
    return plocha, kroky

# Funkce pro výpočet objemu koule
def objem_koule(polomer):
    if polomer <= 0:
        raise ValueError("Poloměr musí být kladné číslo.")
    objem = (4/3) * math.pi * polomer ** 3
    kroky = "Výpočet objemu koule s poloměrem {}: \n".format(polomer) + \
            "Objem = (4/3) * pi * poloměr ** 3 = (4/3) * {} * {} ** 3 = {}".format(math.pi, polomer, objem)
    return objem, kroky

# Nabídka geometrických objektů
print("Vítejte v kalkulačce geometrických objektů!\n"
      "Vyberte si objekt, pro který chcete spočítat plochu nebo objem:\n"
      "1. Kruh\n"
      "2. Obdélník\n"
      "3. Koule")

# Vstup od uživatele
volba = input("Vaše volba: ")

if volba == "1":  # Kruh
    polomer = float(input("Zadejte poloměr kruhu: "))
    try:
        plocha, kroky = plocha_kruhu(polomer)
        print("Plocha kruhu je {}.".format(plocha))
        print(kroky)
    except ValueError as e:
        print(e)
elif volba == "2": # Obdélník
    strana_a = float(input("Zadejte délku strany a obdélníka: "))
    strana_b = float(input("Zadejte délku strany b obdélníka: "))
    try:
        plocha, kroky = plocha_obdelnika(strana_a, strana_b)
        print("Plocha obdélníka je {}.".format(plocha))
        print(kroky)
    except ValueError as e:
        print(e)

elif volba == "3": # Koule
    polomer = float(input("Zadejte poloměr koule: "))
    try:
        objem, kroky = objem_koule(polomer)
        print("Objem koule je {}.".format(objem))
        print(kroky)
    except ValueError as e:
        print(e)

    else:
        print("Neplatná volba. Zvolte prosím 1, 2 nebo 3.")