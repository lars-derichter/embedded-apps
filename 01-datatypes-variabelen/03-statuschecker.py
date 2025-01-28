# 3 waarden (meteen booleans)
temperatuur = 23.5
vochtigheid = 70.0
luchtdruk = 1013.0

# start message: temperatuur
message = f"De temperatuur is {temperatuur}° C. Dat is "

if 20 <= temperatuur <= 25:
    message += "normaal."
elif temperatuur < 20:
    message += "te koud."
else:
    message += "te warm."

# vochtigheid
message += f"\nDe luchtvochtigheid is {vochtigheid}%. Dat is "
if 50 <= vochtigheid <= 90:
    message += "goed."
elif vochtigheid < 50:
    message += "te droog."
else:
    message += "te nat."

# luchtdruk
message += f"\nDe luchtdruk is {luchtdruk} HPa. Dat is "
if 940 <= luchtdruk <= 1060:
    message += "normaal."
elif luchtdruk < 940:
    message += "te laag."
else:
    message += " te hoog."

print(message)