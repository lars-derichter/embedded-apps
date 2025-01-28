# Schrijf deze functions:

# 1. gemiddelde()
#    - Neemt een list van getallen
#    - Geeft het gemiddelde terug

# 2. valideer_sensor_data()
#    - Neemt een list van metingen
#    - Neemt optionele min en max waardes (default 0 en 100)
#    - Geeft terug: aantal geldige metingen, aantal ongeldige metingen

# Test je code:
temperaturen = [18.5, 23.4, 25.0, -2.0, 24.8, 150.5]

def gemiddelde(getallen):
    if len(getallen) == 0: # deling door 0 voorkomen
        return 0
    return sum(getallen) / len(getallen)

def valideer_sensor_data(metingen, min_waarde=0, max_waarde=100):
    geldig = 0
    ongeldig = 0
    
    for meting in metingen:
        if min_waarde <= meting <= max_waarde:
            geldig += 1
        else:
            ongeldig += 1
    
    return geldig, ongeldig

# Test gemiddelde
gem = gemiddelde(temperaturen)
print(f"Gemiddelde temperatuur: {gem:.1f}°C")

# Test validatie (met aangepaste grenswaarden)
geldig, ongeldig = valideer_sensor_data(temperaturen, 15, 30)
print(f"Geldige metingen: {geldig}")
print(f"Ongeldige metingen: {ongeldig}")
