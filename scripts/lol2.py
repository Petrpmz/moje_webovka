def do_slovniku(seznam_slov):
    typy = []
    for slovo in seznam_slov:
        if slovo in ("a", "ne", "on", "já"):
            typy.append(slovo)
    return typy
tokeny = ["ne", "ne", "ne", "on", "ne", "já", "upéci", "dikobraz", "a", "dikobraz"]
typy = do_slovniku(tokeny)
print(typy)
