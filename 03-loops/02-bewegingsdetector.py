import random
max_checks = 10
beweging_gevonden = False

for check_nummer in range(max_checks):
    print(f"Check {check_nummer + 1}...")

    # Simuleer 20% kans op beweging
    if random.random() < 0.2:  # geeft getal tussen 0 en 1
        print("Beweging gedetecteerd!")
        beweging_gevonden = True
        break

    # Kleine pauze voor het effect
    print("Geen beweging...")

if not beweging_gevonden:
    print("Timeout: geen beweging gedetecteerd")