# Opdracht 1 modules
# Naam student:
# Groep:

# import .....
# for line in open("test.csv", 'rt'):
#   jouw code komt hier!
# Opdracht 1 functies
# Naam student:
# Groep:

from modules import csv  # Importeer de functie uit je module

def filter(personen, filterveld, filterwaarde):
    """
    Filtert een lijst van personen op basis van een veld en een filterwaarde.
    
    :param personen: lijst van dictionaries met gegevens van personen
    :param filterveld: het veld waarop gefilterd moet worden (bijv. 'voornaam', 'plaats')
    :param filterwaarde: de waarde waarmee gefilterd moet worden
    :return: gefilterde lijst van personen
    """
    gefilterd = []
    for persoon in personen:
        if persoon.get(filterveld, "").lower().startswith(filterwaarde.lower()):
            gefilterd.append(persoon)
    return gefilterd

# Test de functie
if __name__ == "__main__":
    personen = get_personen()  # Haal de lijst van personen op uit je module
    print("Filter op voornaam 'Ja':")
    resultaat = filter(personen, "voornaam", "Ja")
    for persoon in resultaat:
        print(f"{persoon['voornaam']} {persoon['achternaam']}")

    print("\nFilter op plaats 'd':")
    resultaat = filter(personen, "plaats", "d")
    for persoon in resultaat:
        print(f"{persoon['voornaam']} {persoon['achternaam']}")