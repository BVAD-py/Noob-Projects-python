
characters = [
    {"name": "Luffy", "power_level": 1500},
    {"name": "Eren", "power_level": 1200},
    {"name": "Naruto", "power_level": 3000},
    {"name": "Zoro", "power_level": 1400},
    {"name": "Sasuke", "power_level": 2800},
    {"name": "Itachi", "power_level": 3500},
    {"name": "Goku", "power_level": 5000},
    {"name": "Vegeta", "power_level": 4800},
    {"name": "Ichigo", "power_level": 3200},
    {"name": "Levi", "power_level": 1700},
    {"name": "Gojo", "power_level": 6000},
    {"name": "Deku", "power_level": 1600},
]

names = [c["name"]for c in characters ]   #list comprehension makes list of new strings 

characters.sort(key = lambda c: c["power_level"])

for i, c in enumerate(characters, 1):
    print(f"{i} {c['name']} - {c['power_level']}")






