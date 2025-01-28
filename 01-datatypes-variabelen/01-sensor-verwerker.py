# temperatuur als string (probeer met verschillende waarden)
temp_string = "26"

# omzetten naar float
temp = float(temp_string)

# start van het bericht (met f-string)
message = f"Temperatuur is {temp_string}° C. Dat is "

# testen of de temperatuur goed is
if 20 <= temp <= 25:
    message += "goed." # stukje toevoegen aan message
elif temp < 20:
    message += "te koud."
else:
    message += "te warm."

print(message) # message tonen