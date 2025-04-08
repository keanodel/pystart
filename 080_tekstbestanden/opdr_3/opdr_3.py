# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def encrypt(tekst, verschuiving):
    """Versleutel de tekst door elke letter te verschuiven."""
    resultaat = ""
    for char in tekst:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            nieuwe_char = chr((ord(char) - ascii_offset + verschuiving) % 26 + ascii_offset)
            resultaat += nieuwe_char
        else:
            resultaat += char
    return resultaat

def decrypt(tekst, verschuiving):
    """Ontsleutel de tekst door elke letter terug te verschuiven."""
    return encrypt(tekst, -verschuiving)


originele_tekst = input("Voer een tekst in om te versleutelen: ")


versleutelde_tekst = encrypt(originele_tekst, 5)
print(f"Versleutelde tekst: {versleutelde_tekst}")

ontsleutelde_tekst = decrypt(versleutelde_tekst, 5)
print(f"Ontsleutelde tekst: {ontsleutelde_tekst}")



