from zaidimo_struktura import main
from funkcijos import vieta

while True:
    vieta = [x for x in range(1, 10)]  #pridetas i while True kad pradedant iš naujo, pradetu nuo pirminės reiksmes
    main()
    uzklausimas = input("Ar norite sužaisti dar kartą? Spausti T pradėti, bet kokį mygtuką - išeiti ")
    if uzklausimas == "T":
        continue
    else:
        print("Ačiū už žaidimą.Viso gero...")
        break