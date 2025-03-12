# Python basis

### functies
Deze opdracht hoort bij de cursus python op [edutorial.nl](https://www.edutorial.nl/course/python)

### Opdracht

* Maak gebruik van het bestand: opdr_4.py
* Pas de code aan van opdr_4.py
* Commit en push je code naar github of bewaar in onedrive


Schrijf een functie die een lijst met dictionaries accepteert.
Iedere dictionary bestaat uit 3 elementen:
* voornaam
* tussenvoegsel
* achternaam

```python
def volledige_naam(lijst_met_namen):
    # hier komt jouw code
    pass

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
```

Output
> Willem van Dijk  
Klaas Wopstra  
Miep van der Plas  
Carla Hoogvliet  

LET OP: Er mogen geen dubbele spaties zitten tussen de voor- en achternaam!!