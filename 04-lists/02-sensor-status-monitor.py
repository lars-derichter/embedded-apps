# Sensor statussen ("OK" of "ERROR")
statussen = ["OK", "ERROR", "OK", "OK", "ERROR", "OK", "ERROR"]

# Opdrachten:
# 1. Tel hoeveel sensoren OK zijn
# 2. Vind de positie van de eerste ERROR
# 3. Maak een nieuwe list met alleen de laatste 3 statussen
# 4. Vervang alle "ERROR" statussen door "FOUT"

# Tel OK sensoren
aantal_ok = statussen.count("OK")
print(f"Aantal werkende sensoren: {aantal_ok}")

# Vind eerste ERROR
eerste_error = statussen.index("ERROR")
print(f"Eerste ERROR op positie: {eerste_error}")

# Laatste 3 statussen
laatste_drie = statussen[-3:]
print(f"Laatste drie statussen: {laatste_drie}")

# Vervang ERROR door FOUT
nieuwe_statussen = ["FOUT" if s == "ERROR" else s for s in statussen]
print(f"Nieuwe statussen: {nieuwe_statussen}")
