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

def filter(data, filterveld, filterwaarde):
    """
    Filtert een lijst van CSV-regels op basis van een veld en een filterwaarde.
    """
    header = data[0].strip().split(",")
    if filterveld not in header:
        raise ValueError(f"Filterveld '{filterveld}' bestaat niet in de data.")

    veld_index = header.index(filterveld)
    gefilterde_data = []

    for regel in data[1:]:
        waarden = regel.strip().split(",")
        if waarden[veld_index].lower().startswith(filterwaarde.lower()):
            gefilterde_data.append(regel.strip())

    return gefilterde_data