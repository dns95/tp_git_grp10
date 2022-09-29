# Créé par Ami, le 06/09/2022 en Python 3.7
Celcius = 0
Farheineit = 0
Température = int(input("Saissisez une température : "))
choix = int(input("Taper 1 pour la conversion en Celcius \nTaper 2 pour une conversion en Farheineit"))
if choix == 1:
    Farheineit = Température
    ConversionCelcius = (Farheineit - 32) * 5/9
    print("Le nombre saisi en température Celcius est de ", ConversionCelcius)
elif choix == 2:
    Celcius = Température
    ConversionFarheineit = (Celcius * 9/5) + 32
    print("Le nombre saisi en température Farheineit est de", ConversionFarheineit)
elif choix >1:
    print("Saisi incorrect")
elif choix <2:
    print("Saisi incorrect")



