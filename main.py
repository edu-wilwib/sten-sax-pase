import random as rand

datornamn = "Python"
print(f"Nu ska vi spela Sten, Sax eller Påse!\nJag är {datornamn}.")
spelarnamn = input("\nAnge ditt spelarnamn -> ")
antal_omgångar = int(input("Ange antal omgångar vi ska spela -> "))

for i in range(antal_omgångar):
    print(f"Spelomgång {i+1}\n{15*'-'}")
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
            vinnare = None
        elif dator_drag == "Sax":
            vinnare = spelarnamn
        else:
            vinnare = datornamn
    elif drag == "Sax":
        if dator_drag == "Sten":
            vinnare = datornamn
        elif dator_drag == "Sax":
            vinnare = None
        else:
            vinnare = spelarnamn
    else:
        if dator_drag == "Sten":
            vinnare = spelarnamn
        elif dator_drag == "Sax":
            vinnare = datornamn
        else:
            vinnare = None
    if vinnare:
        print(f"Vinnare i spelomgång {i+1}: {vinnare}")
    else:
        print("Oavgjort.")