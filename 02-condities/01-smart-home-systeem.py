# Sensor waardes
temperatuur = 24
luchtvochtigheid = 65
licht_niveau = 800    # in lux
beweging = True       # bewegingssensor
tijd = 14            # uur van de dag (24-uurs formaat)

# 1. Bepaal de temperatuur status
# - Onder 18: "verwarming aan"
# - 18-24: "temperatuur OK"
# - Boven 24: "koeling aan"

# 2. Check luchtvochtigheid
# - Boven 60: "te vochtig"
# - 40-60: "prima"
# - Onder 40: "te droog"

# 3. Bepaal of het licht aan moet
# Voorwaarden voor licht aan:
# - Als het donker is (licht_niveau < 100)
# - OF als er beweging is EN het tussen 8 en 22 uur is

# 1. Temperatuur status
if temperatuur < 18:
    temp_status = "verwarming aan"
elif temperatuur <= 24:
    temp_status = "temperatuur OK"
else:
    temp_status = "koeling aan"

print(f"Temperatuur {temperatuur}°C: {temp_status}")

# 2. Luchtvochtigheid check
if luchtvochtigheid > 60:
    vocht_status = "te vochtig"
elif luchtvochtigheid >= 40:
    vocht_status = "prima"
else:
    vocht_status = "te droog"

print(f"Luchtvochtigheid {luchtvochtigheid}%: {vocht_status}")

# 3. Licht controle
licht_nodig = licht_niveau < 100 or (beweging and 8 <= tijd <= 22)
print(f"Licht moet {'aan' if licht_nodig else 'uit'}") 

# in een f-string kan dus ook een klein stukje code
