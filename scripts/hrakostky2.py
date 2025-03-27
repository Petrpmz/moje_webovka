#Královský paš a zlá sedmička 
import random

player1_rolls=[]
player2_rolls=[]
rolls=len(player1_rolls)+len(player2_rolls)

print("1. Pravidla")
print("2. Začít hru")
print("3. Ukončit hru")
choice = int(input("Zadej svoji volbu: "))


if choice == 1:
    print("Pravidla hry jsou:")
    print("- Každý hráč hazí dvouma kostkama.")
    print("- Jestli hodí dohramdy 7, prohrál.")
    print("- Jestli hodí dvě stejná čísla, vyhrál.")
    print("- Hra pokračuje, dokud jeden hráč nevyhraje nebo neprohraje.")
    while True:
        print("1. Pravidla")
        print("2. Začít hru")
        print("3. Ukončit hru")
        choice = int(input("Zadej svoji volbu: "))
        if choice == 1:
            print("Pravidla hry jsou:")
            print("- Každý hráč hazí dvouma kostkama.")
            print("- Jestli hodí dohramdy 7, prohrál.")
            print("- Jestli hodí dvě stejná čísla, vyhrál.")
            print("- Hra pokračuje, dokud jeden hráč nevyhraje nebo neprohraje.")
        elif choice==2:
            player1_name = input("Zadej jméno prvního hráče: ")
            player2_name = "Druhý hráč"
            while True:
                rolls=len(player1_rolls)+len(player2_rolls)
                print((player1_name), "hází kostkou...")
                input("Zmáčkni Enter pro hod kostkou...")
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                player1_rolls.append(dice1)
                player1_rolls.append(dice2)
                print((player1_name),"hodil",(dice1),"a",(dice2))
                if dice1 + dice2 == 7:
                    print((player1_name),"prohrál")
                    print(rolls)
                    break
                elif dice1 == dice2:
                    print((player1_name),"vyhrál")
                    print(rolls)
                    break

                print((player2_name),"hází kostkou...")
                input("Zmáčkni Enter pro hod kostkou...")
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                player2_rolls.append(dice1)
                player2_rolls.append(dice2)
                print((player2_name),"hodil",(dice1),"a",(dice2))
                if dice1 + dice2 == 7:
                    print((player2_name),"prohrál")
                    print(rolls)
                    break
                elif dice1 == dice2:
                    print((player2_name),"vyhrál")
                    print(rolls)
                    break
        elif choice == 3:
            break
        else:
            print("Nesprávná volba.")

elif choice==2:
    player1_name = input("Zadej jméno prvního hráče: ")
    player2_name = "Druhý hráč"
    while True:
        print((player1_name), "hází kostkou...")
        input("Zmáčkni Enter pro hod kostkou...")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        player1_rolls.append(dice1)
        player1_rolls.append(dice2)
        print((player1_name),"hodil",(dice1),"a",(dice2))
        if dice1 + dice2 == 7:
            print((player1_name),"prohrál")
            print(rolls/2)
            break
        elif dice1 == dice2:
            print((player1_name),"vyhrál")
            print(rolls/2)
            break

        print((player2_name),"hází kostkou...")
        input("Zmáčkni Enter pro hod kostkou...")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        player2_rolls.append(dice1)
        player2_rolls.append(dice2)
        print((player2_name),"hodil",(dice1),"a",(dice2))
        if dice1 + dice2 == 7:
            print((player2_name),"prohrál")
            print(rolls/2)
            break
        elif dice1 == dice2:
            print((player2_name),"vyhrál")
            print(rolls/2)
            break
    while True:
        if choice == 3:
            break
        else:
            print("Nesprávná volba.")
