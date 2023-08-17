import pickle


vieta = [x for x in range(1, 10)]

x_rezultatas = []
o_rezultatas = []


def vietos_atstatymas():
    """
    Funkcija skirta atstatyti zaidimo tinklelį, pradėjus naują žaidimo seriją.
    """
    global vieta
    vieta = [x for x in range(1, 10)]


def zaidimo_tinklelis():
    """
        susideliojama vietos į tinklelį 3x3,
        priskiriant masyvo indeksui jo vietą.
        """
    lenta = (
        f"   {vieta[0]} | {vieta[1]} | {vieta[2]} \n"
        f"   {vieta[3]} | {vieta[4]} | {vieta[5]} \n"
        f"   {vieta[6]} | {vieta[7]} | {vieta[8]}")
    return lenta


def zaidejo_ejimas(zaidejas):
    """
    Funkcija skirta atvaizduoti žaidėjų ėjimus žaidimo tinklelyje.
    :param zaidejas: X arba O
    :return:
    """
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
    """
       Išvardinti visi galimi laimėjimo būdai. Žaidėjui X arba O užėmus nors vieną iš aštuonių kombinacijų
       grąžinamas rezultatas True.
       """
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
    """
       Jei nei vienas žaidėjęs dar nelaimėjo, ėjimai daromi tol kol žaidimo tinklelyje nebelieka skaitmenų.
       Kai žaidėjai užima visas galimas vietas ir nėra skelbiamas laimėtojas, tik tokiu atvejus funkcija grąžins True.
       """
    for uzimta in vieta:
        if (uzimta == 1 or uzimta == 2 or uzimta == 3 or uzimta == 4
                or uzimta == 5 or uzimta == 6 or uzimta == 7 or uzimta == 8):
            return False
    else:
        return True


def rezultatai():
    """
      Funkcija fiskuoja žaidimų laimėjimus į X žaidėjo laimėjimų žurnalą, ir į O žaidėjo laimėjimų žurnalą.
      Po kiekvieno žaidimo, funkcija nuskaito abiejų žurnalų duomenis ir grąžina iki šiol sužaistų serijų rezultatus.
      """
    x_rezultatas = []
    o_rezultatas = []
    try:
        with open("x_rezultatas.pkl", "rb") as file:
             pickle.load(file)
        with open("o_rezultatas.pkl", "rb") as file:
            pickle.load(file)
    except:
        with open("x_rezultatas.pkl", "wb") as file:
            pickle.dump(x_rezultatas, file)
        with open("o_rezultatas.pkl", "wb") as file:
             pickle.dump(o_rezultatas, file)
    if laimejimas("X"):
        with open("x_rezultatas.pkl", "rb") as file:
            x_rezultatas = pickle.load(file)
            with open("x_rezultatas.pkl", "wb") as file:
                 x_rezultatas.append(1)
                 pickle.dump(x_rezultatas, file)
            with open("o_rezultatas.pkl", "rb") as file:
                o_rezultatas = pickle.load(file)
    if laimejimas("O"):
        with open("o_rezultatas.pkl", "rb") as file:
            o_rezultatas = pickle.load(file)
            with open("o_rezultatas.pkl", "wb") as file:
                 o_rezultatas.append(1)
                 pickle.dump(o_rezultatas, file)
            with open("x_rezultatas.pkl", "rb") as file:
                x_rezultatas = pickle.load(file)
    if lygios:
        with open("x_rezultatas.pkl", "rb") as file:
            x_rezultatas = pickle.load(file)
        with open("o_rezultatas.pkl", "rb") as file:
            o_rezultatas = pickle.load(file)
    rezultatasx = sum(x_rezultatas)
    rezultataso = sum(o_rezultatas)
    return f"Rezultatai: X:{rezultatasx} - O:{rezultataso}"