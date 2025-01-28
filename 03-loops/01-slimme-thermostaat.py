# for werkt niet, want step moet integer zijn

temperatuur = 18.0

while temperatuur < 22:
    if temperatuur == int(temperatuur):
        print(f"gehele graad bereikt: {temperatuur}")
    print(f"temperatuur: {temperatuur}") # om te checken of dit wel wordt uitgevoerd
    temperatuur += 0.5
