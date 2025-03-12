# Python basis

### Lists
Deze opdracht hoort bij de cursus python op [edutorial.nl](https://www.edutorial.nl/course/python)

### Opdracht
Maak gebruik van het bestand: opdr_2.py
* Pas de code aan van opdr_2.py
* Commit en push je code naar github of bewaar in onedrive

Maak een dictionary met een aantal grote rivieren en de landen waar ze doorheen stromen
Bij deze opdracht heb je ook een lijst nodig met de landen waar de rivieren door stromen.
Die lijst kun je zo maken:
```python
rivier_info = { 
    "rijn": ["nederland", "duitsland", "Frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

```

Print de naam van de 1e rivier  
Print het 2e land waar de 1e rivier doorheen stroomt
Zowel land als rivier beginnen met een hoofdletter, gebruik hiervoor een tekstfunctie. 

> Gebruik bij alle opdrachten deze code rivieren[?]. Vul in wat er op de plek van het vraagteken moet komen.  
> Gebruik ook deze code rivier_info[?][?]. Vul in wat er op de plek van de vraaktekens moet komen.

Output:  
>De rivier Rijn stroomt onder andere door Duitsland

Print de naam van de 2e rivier  
Print het 1e land waar de 1e rivier doorheen stroomt
Zowel land als rivier beginnen met een hoofdletter 

Output:  

>De rivier Maas stroomt onder andere door Nederland

Print de naam van de 3e rivier  
Print het 3e land waar de 3e rivier doorheen stroomt
Zowel land als rivier beginnen met een hoofdletter 

Output:  

>De rivier Nijl stroomt onder andere door Oeganda

