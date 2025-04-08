# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
# Vragenlijst
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]


feestgangers = []

while True:
    print("Vul de volgende vragen in:")
    antwoorden = {} 

    for i, vraag in enumerate(vragen, start=1):
        antwoord = input(f"{i}. {vraag} ")
        if i == 1:
            antwoorden["voornaam"] = antwoord
        elif i == 2:
            antwoorden["achternaam"] = antwoord
        elif i == 3:
            antwoorden["drank"] = antwoord
        elif i == 4:
            antwoorden["eten"] = antwoord

    feestgangers.append(antwoorden) 

    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")


    doorgaan = input("Wil je nog een feestganger toevoegen? (ja/nee) ").strip().lower()
    if doorgaan != "ja":
        break


with open("feestgangers.txt", "w") as bestand:
    for feestganger in feestgangers:
        bestand.write("----\n")
        for key, value in feestganger.items():
            bestand.write(f"{key}: {value}\n")
        bestand.write("\n")

print("De gegevens zijn opgeslagen in 'feestgangers.txt'.")