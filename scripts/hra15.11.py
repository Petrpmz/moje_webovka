x=21
y=0
while x!=y:
    c=int(input("První hráč bere 1, 2 nebo 3 sirky?"))
    if c>=4 or c>x:
        print("Maximalně tři.")
        break
    x-=c
    if x==y:
        print("Vyhrál druhý hráč.")
        break
    print("Zbývá",x,"sirek.")
    d=int(input("Druhý hráč bere 1, 2 nebo 3 sirky?"))
    if d>=4 or d>x:
        print("Můžete vzít maximlně 3 sirky")
        break
    x-=d
    if x==y:
        print("Vyhrál první hráč.")
        break
    print("Zbývá",x,"sirek.")

