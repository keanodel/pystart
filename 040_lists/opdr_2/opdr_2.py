# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....
print(rivieren[0]) #print de eerste rivier, de rijn.
print(rivier_info[rivieren[0]][0])
caps = f"{rivieren[2].capitalize()} {rivier_info[rivieren[2]][2].capitalize()}"
print(caps)