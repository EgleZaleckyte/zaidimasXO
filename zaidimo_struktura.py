from funkcijos import zaidimo_tinklelis, zaidejo_ejimas, laimejimas, lygios


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
