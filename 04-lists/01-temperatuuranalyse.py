# Temperatuurmetingen over een dag
temps = [18.5, 19.2, 22.1, 23.4, 25.0, 24.8, 23.2, 21.5]

# Opdrachten:
# 1. Print de hoogste en laagste temperatuur
# 2. Bereken het gemiddelde
# 3. Tel hoeveel metingen boven de 23 graden zijn
# 4. Maak een nieuwe list met alleen de middag metingen (index 4-7)

# Hoogste en laagste temperatuur
max_temp = max(temps)
min_temp = min(temps)
print(f"Hoogste temperatuur: {max_temp}°C")
print(f"Laagste temperatuur: {min_temp}°C")

# Gemiddelde berekenen
gemiddelde = sum(temps) / len(temps)
print(f"Gemiddelde temperatuur: {gemiddelde:.1f}°C") # :.1f 1cijfer na de komma

# Metingen boven 23 graden tellen
hoge_temps = [t for t in temps if t > 23]
aantal_hoog = len(hoge_temps)
print(f"Aantal metingen boven 23°C: {aantal_hoog}")

# Of de simpele minder Pythonachtige manier
aantal_hoge_temps = 0
for positie in range(0, len(temps), 1):
    if temps[positie] > 23:
        aantal_hoge_temps += 1
print(f"Aantal metinegen boven 23°C: {aantal_hoge_temps}")

# Middag metingen
middag = temps[4:8]
print(f"Middag temperaturen: {middag}")