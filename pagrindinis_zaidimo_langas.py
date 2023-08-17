from zaidimo_logika import zaidimo_logika
from funkcijos import rezultatai, vietos_atstatymas
import pickle

x_rezultatas = []
o_rezultatas = []

while True:
    vietos_atstatymas()
    zaidimo_logika()
    print(rezultatai())
    uzklausimas = input("Ar norite sužaisti dar kartą? Spausti T pradėti, bet kokį mygtuką - išeiti ")
    if uzklausimas == "T":
        continue
    else:
        print("Ačiū už žaidimą.Viso gero...")
        with open("x_rezultatas.pkl", "wb") as file:
            x_rezultatas.clear()
            pickle.dump(x_rezultatas, file)
        with open("o_rezultatas.pkl", "wb") as file:
            o_rezultatas.clear()
            pickle.dump(o_rezultatas, file)
        break
