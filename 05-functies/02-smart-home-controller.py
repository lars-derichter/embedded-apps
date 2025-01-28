# Schrijf deze functions:

# 1. bereken_energie_status()
#    - Parameters: temperatuur, licht_aan (True/False)
#    - Return: "HOOG", "MEDIUM" of "LAAG" energieverbruik

# 2. genereer_systeem_rapport()
#    - Parameters: temperatuur, luchtvochtigheid, licht_status
#    - Return: string met complete status rapport
#    - Gebruik bereken_energie_status() in deze function

# Test je code:
temp = 23.5
vocht = 65
licht = True

def bereken_energie_status(temp, is_licht_aan):
    if temp < 25 and not is_licht_aan:
        return "LAAG"
    elif temp > 25 and is_licht_aan:
        return "HOOG"
    else:
        return "MEDIUM"
    
def genereer_systeem_rapport(temp, vocht, is_licht_aan):
    energiestatus = bereken_energie_status(temp, is_licht_aan)
    rapport = f"De temperatuur is {temp}° C\n"
    rapport += f"De luchtvochtigheid is {vocht} %\n"
    rapport += f"Het energieverbruik is {energiestatus}"
    return rapport


# test energiestatus
print(f"energiestatus is {bereken_energie_status(temp, licht)}")

# test rapport
print(genereer_systeem_rapport(temp, vocht, licht))