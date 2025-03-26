# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
import math

a = float(input("Voer de lengte van zijde a in: "))
b = float(input("Voer de lengte van zijde b in: "))

# Bereken de lengte van de hypotenusa (c) met de stelling van Pythagoras: c² = a² + b²
c = math.sqrt(a**2 + b**2)

# Print het resultaat
print(f"De lengte van de schuine zijde is: {c:.2f}")