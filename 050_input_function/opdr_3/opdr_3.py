# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

import sys

gebruiker = input("Voer maximaal 5 woorden in, deze worden op omgekeerde alfabethische volgorde gesorteerd: ")
woord = gebruiker.split(',')
woord = [w.strip() for w in woord]

if len(woord) > 5:
    sys.exit("Je hebt teveel woorden ingevoerd! Het limiet is 5.")

    woord = woord[:5]

woord_reverse = sorted(woord, reverse=True)
print("Hier zijn de woorden gesorteerd van Z naar A:", woord_reverse)