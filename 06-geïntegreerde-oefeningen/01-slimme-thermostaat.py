def genereer_meting(basis_temp, variatie):
    # Simuleer een temperatuur meting met wat variatie
    return basis_temp + (variatie * random.random())

def analyseer_temperaturen(metingen, min_temp=18, max_temp=24):
    # Analyseer een lijst van temperatuur metingen
    gemiddelde = sum(metingen) / len(metingen)
    minimum = min(metingen)
    maximum = max(metingen)
    te_koud = 0
    te_warm = 0
    correct = 0
    
    for temp in metingen:
        if temp < min_temp:
            te_koud += 1
        elif temp > max_temp:
            te_warm += 1
        else:
            correct += 1
            
    return gemiddelde, minimum, maximum, te_koud, te_warm, correct

def bepaal_actie(temperaturen):
    gemiddelde, minimum, maximum, te_koud, te_warm, correct = analyseer_temperaturen(temperaturen)
    # Bepaal welke actie nodig is op basis van analyse
    if te_koud > te_warm:
        return "Verwarming Verhogen"
    elif te_warm > te_koud:
        return "Koeling Activeren"
    else:
        return "Temperatuur Handhaven"

def print_temperatuur_rapport(metingen):
    gemiddelde, minimum, maximum, te_koud, te_warm, correct = analyseer_temperaturen(metingen)
    actie = bepaal_actie(metingen)
    # Print een geformatteerd rapport
    print("\n=== Temperatuur Rapport ===")
    print(f"Metingen: {[f'{t:.1f}°C' for t in metingen]}")
    print(f"\nStatistieken:")
    print(f"Gemiddelde: {gemiddelde:.1f}°C")
    print(f"Minimum: {minimum:.1f}°C")
    print(f"Maximum: {maximum:.1f}°C")
    print(f"\nStatus:")
    print(f"Te koud: {te_koud} metingen")
    print(f"Te warm: {te_warm} metingen")
    print(f"Correct: {correct} metingen")
    print(f"\nAanbevolen actie: {actie}")

# Hoofdprogramma
import random

# Configuratie
AANTAL_METINGEN = 10
BASIS_TEMP = 21.0
VARIATIE = 4.0

# Metingen simuleren
temperaturen = []
for i in range(AANTAL_METINGEN):
    temp = genereer_meting(BASIS_TEMP, VARIATIE)
    temperaturen.append(temp)
    print(f"Meting {i+1}: {temp:.1f}°C")
    
# Analyse uitvoeren
analyse_resultaat = analyseer_temperaturen(temperaturen)
aanbevolen_actie = bepaal_actie(temperaturen)

# Rapport printen
print_temperatuur_rapport(temperaturen)