# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...
leeftijd_bezoeker = int(input("Wat is de leeftijd van de bezoeker? "))
groep = None
for key, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= leeftijd_bezoeker <= max_leeftijd:
        groep = key
        break
if groep:
    korting = kortings_percentages[groep]
    prijs = normale_toegangsprijs * (1 - korting / 100)
    print(f"U behoort tot de groep {groep}")
    print(f"U krijgt {korting}% korting")
    print(f"U betaalt daarom {prijs:.2f}")
else:
    print("Uw leeftijd valt buiten de toegestane groepen.")