# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier'
vragen =[]
vragen.append(input("Wat vind U van de huidige regering? "))
vragen.append(input("Wat vind je van de Python-lessen tot nu toe? "))
vragen.append(input("Wat vind jij de mooiste stad van Nederland? "))

# Schrijf de antwoorden naar een tekstbestand
with open("vragen.txt", "w") as bestand:  # Open een bestand in schrijfmodus
    for vraag in vragen:
        bestand.write(vraag + "\n")  # Schrijf elk antwoord op een nieuwe regel

print("De antwoorden zijn opgeslagen in 'antwoorden.txt'.")