def sanitize(line):
   # kleine letters maken en spaties voor en na het woord weghalen
   new_lst = []
   lst = line.split(',')
   for item in lst:
       new_lst.append(item.lower().strip())
   return new_lst

def create_person(lst):
    person = {"voornaam": "", "tussenvoegsel": "", "achternaam": ""}
    person["voornaam"] = lst[0]
    person["tussenvoegsel"] = lst[1]
    person["achternaam"] = lst[2]
    return person

def add_fullname(person):
    if person["tussenvoegsel"] == "":
        person['full_name'] = f"{person['voornaam'].title()} {person['achternaam'].title()}"
    else:
        person['full_name'] = f"{person['voornaam'].title()} {person['tussenvoegsel']} {person['achternaam'].title()}"
    return person

def print_persons(persons, filter=["full_name"]):
    counter = 0
    for person in persons:
        counter += 1
        for attr in filter:
            print(person[attr].title(), end=" ")
        print(end="\n")
    print(f"Er zijn in totaal {counter} personen")

def lees_csv(bestandsnaam):
    with open(bestandsnaam, 'r') as bestand:
        return bestand.readlines()

def schrijf_csv(bestandsnaam, data):
    with open(bestandsnaam, 'w') as bestand:
        for regel in data:
            bestand.write(f"{regel}\n")

def filter(personen, filterveld, filterwaarde):
    """
    Filtert een lijst van personen (dictionaries) op basis van een veld en een filterwaarde.
    """
    if not all(filterveld in persoon for persoon in personen):
        raise ValueError(f"Filterveld '{filterveld}' bestaat niet in de data.")

    gefilterde_personen = [
        persoon for persoon in personen
        if persoon[filterveld].lower().startswith(filterwaarde.lower())
    ]

    return gefilterde_personen

def get_personen():
    """
    Retourneert een lijst van personen als dictionaries.
    """
    return [
        {"voornaam": "Jan", "achternaam": "Van Der Vliet", "plaats": "Amsterdam"},
        {"voornaam": "Jan Jaap", "achternaam": "Siewers", "plaats": "Den Haag"},
        {"voornaam": "Piet", "achternaam": "De Vries", "plaats": "Rotterdam"},
        {"voornaam": "Griet", "achternaam": "Van Der Pol", "plaats": "Delft"},
    ]