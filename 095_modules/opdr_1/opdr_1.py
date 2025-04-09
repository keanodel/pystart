# Opdracht 1 functies
# Naam student:
# Groep:

def lees_csv(bestandsnaam):
    with open(bestandsnaam, 'r') as bestand:
        return bestand.readlines()

def schrijf_csv(bestandsnaam, data):
    with open(bestandsnaam, 'w') as bestand:
        for regel in data:
            bestand.write(f"{regel}\n")


data = ["Naam,Leeftijd,Stad", "Willem,30,Amsterdam", "Klaas,25,Rotterdam"]
schrijf_csv("output.csv", data)

from modules import csv

gelezen_data = lees_csv("output.csv")
print("Inhoud van het CSV-bestand:")
for regel in gelezen_data:
    print(regel.strip())