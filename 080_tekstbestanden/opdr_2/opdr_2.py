# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

prompt = "Raad mijn geheime getal (tussen 1 en 100): \n"
geheim_getal = random.randint(1, 100)
pogingen = 0
while True:
    try:
        gok = int(input(prompt))
        pogingen += 1 
        if gok < geheim_getal:
            print("Hoger!")
        elif gok > geheim_getal:
            print("Lager!")
        else:
            print(f"Gefeliciteerd! Je hebt het geheime getal {geheim_getal} geraden.")
            print(f"Je hebt {pogingen} pogingen nodig gehad.")
            break
    except ValueError:
        print("Voer een geldig getal in!")