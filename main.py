vieta = [x for x in range(1, 10)]


def zaidimo_tinklelis():
    # susideliojama vietos į tinklelį 3x3, priskiriant masyvo indeksui jo vietą.
    lenta = (
        f"   {vieta[0]} | {vieta[1]} | {vieta[2]} \n"
        f"   {vieta[3]} | {vieta[4]} | {vieta[5]} \n"
        f"   {vieta[6]} | {vieta[7]} | {vieta[8]}")
    return lenta


def zaidejo_ejimas(zaidejas):
    zaidejas == "X" or zaidejas == "O"
    while True:
       try:
           ejimas = int(input(f"žaidėjas {zaidejas} :pasirinkite veiksmą: "))
        # kad ejimas atitiktu indeksa reikia atimti 1, nes paspaudus 1, turi pasikeisti index 0 vieta.
           if type(vieta[ejimas - 1]) == int:
               vieta[ejimas - 1] = zaidejas
               break
           else:
               print("ši vieta jau užimta, rinkitės laisvą vietą")
       except ValueError:
               print("Įveskite laisvą skaičių nuo 1 iki 9")


def laimejimas(zaidejas):
    if (zaidejas == vieta[0] and zaidejas == vieta[1] and zaidejas == vieta[2] or
            zaidejas == vieta[3] and zaidejas == vieta[4] and zaidejas == vieta[5] or
            zaidejas == vieta[6] and zaidejas == vieta[7] and zaidejas == vieta[8] or
            zaidejas == vieta[0] and zaidejas == vieta[3] and zaidejas == vieta[6] or
            zaidejas == vieta[1] and zaidejas == vieta[4] and zaidejas == vieta[7] or
            zaidejas == vieta[2] and zaidejas == vieta[5] and zaidejas == vieta[8] or
            zaidejas == vieta[0] and zaidejas == vieta[4] and zaidejas == vieta[8] or
            zaidejas == vieta[2] and zaidejas == vieta[4] and zaidejas == vieta[6]):
        return True
    else:
        return False


def lygios():
    for uzimta in vieta:
        if (uzimta == 1 or uzimta == 2 or uzimta == 3 or uzimta == 4
            or uzimta == 5 or uzimta == 6 or uzimta == 7 or uzimta == 8):
            return False
    else:
        return True


def main():
    while True:
        print(zaidimo_tinklelis())
        zaidejo_ejimas("X")
        print(zaidimo_tinklelis())
        if laimejimas("X"):
            print("Žaidėjas X laimėjo !")
            break
        elif lygios():
            print("Sužaidėte lygiosiomis")
            break
        zaidejo_ejimas("O")
        if laimejimas("O"):
            print(zaidimo_tinklelis())
            print("Žaidėjas O laimėjo !")
            break
        elif lygios():
            print(" Sužaidėte lygiosiomis")
            break


while True:
    vieta = [x for x in range(1, 10)]  #pridetas i while True kad pradedant iš naujo, pradetu nuo pirminės reiksmes
    main()
    uzklausimas = input("Ar norite sužaisti dar kartą? Spausti T pradėti, bet kokį mygtuką - išeiti ")
    if uzklausimas == "T":
        continue
    else:
        print("Ačiū už žaidimą.Viso gero...")
        break

