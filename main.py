import random as rand

datornamn = "Python"
print(f"Nu ska vi spela Sten, Sax eller Påse!\nJag är {datornamn}.")
spelarnamn = input("\nAnge ditt spelarnamn -> ")
while True:
    antal_omgångar = input("Ange antal omgångar vi ska spela -> ")
    try:
        int(antal_omgångar)
    except ValueError:
        continue
    break
antal_omgångar = int(antal_omgångar)
spelarpoäng = 0
datorpoäng = 0

for i in range(antal_omgångar):
    print(f"\n\nSpelomgång {i+1}\n{15*'-'}")
    while True:
        drag = input("Välj 'Sten', Sax' eller 'Påse' -> ")
        if drag.lower() == "sten":
            drag = "Sten"
        elif drag.lower() == "sax":
            drag = "Sax"
        elif drag.lower() == "påse":
            drag = "Påse"
        else:
            print("Ogiltigt drag. Försök igen.")
            continue
        break
    print(f"{spelarnamn} spelar: {drag}")
    dator_drag = rand.randint(1, 3)
    if dator_drag == 1:
        dator_drag = "Sten"
    elif dator_drag == 2:
        dator_drag = "Sax"
    else:
        dator_drag = "Påse"
    print(f"{datornamn} spelar: {dator_drag}")
    if drag == "Sten":
        if dator_drag == "Sten":
            vinnare = "Oavgjort"
        elif dator_drag == "Sax":
            vinnare = spelarnamn
        else:
            vinnare = datornamn
    elif drag == "Sax":
        if dator_drag == "Sten":
            vinnare = datornamn
        elif dator_drag == "Sax":
            vinnare = "Oavgjort"
        else:
            vinnare = spelarnamn
    else:
        if dator_drag == "Sten":
            vinnare = spelarnamn
        elif dator_drag == "Sax":
            vinnare = datornamn
        else:
            vinnare = "Oavgjort"
    print(f"\nVinnare i spelomgång {i+1}: {vinnare}!")
    if vinnare == spelarnamn:
        spelarpoäng += 1
    elif vinnare == datornamn:
        datorpoäng += 1

print(f"SLUTRESULTAT\n{13*'='}")
if spelarpoäng > datorpoäng:
    print(f"{spelarnamn}: {spelarpoäng}p")
    print(f"{datornamn}: {datorpoäng}p")
    print(f"\nVinnare: {spelarnamn}")
elif datorpoäng > spelarpoäng:
    print(f"{datornamn}: {datorpoäng}p")
    print(f"{spelarnamn}: {spelarpoäng}p")
    print(f"\nVinnare: {datornamn}")
else:
    print(f"\nVinnare: Oavgjort!")

print("Programmet avslutades normalt.")