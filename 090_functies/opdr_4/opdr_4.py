# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        tussenvoegsel = f" {naam['tussenvoegsel']}" if naam['tussenvoegsel'] else ""
        volledige_naam = f"{naam['voornaam']}{tussenvoegsel} {naam['achternaam']}"
        print(volledige_naam)


namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)