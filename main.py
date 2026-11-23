import random as rand

datornamn = "Python"
print(f"Nu ska vi spela Sten, Sax eller Påse!\nJag är {datornamn}.")
spelarnamn = input("\nAnge ditt spelarnamn -> ")
while True: #säker inmatning
    antal_omgångar = input("Ange antal omgångar vi ska spela -> ")
    try:
        int(antal_omgångar) #kollar att det är ett heltal
    except ValueError:
        continue #om det inte är det får man skriva något annat
    break
antal_omgångar = int(antal_omgångar) #gör den från str till int
spelarpoäng = 0
datorpoäng = 0

for i in range(antal_omgångar): #loopen körs en gång per omgång
    print(f"\n\nSpelomgång {i+1}\n{15*'-'}") #skriver vilken omgång man är på
    while True: #säker inmatning
        drag = input("Välj 'Sten', Sax' eller 'Påse' -> ") 
        if drag.lower() == "sten": #skriver om så att endast första bokstaven är stor
            drag = "Sten"
        elif drag.lower() == "sax": #samma som ovan
            drag = "Sax"
        elif drag.lower() == "påse": #samma som ovan
            drag = "Påse"
        else:
            print("Ogiltigt drag. Försök igen.")
            continue
        break
    print(f"{spelarnamn} spelar: {drag}") #skriver spelarens drag
    dator_drag = rand.randint(1, 3) #slumpar fram datorns drag
    if dator_drag == 1:
        dator_drag = "Sten"
    elif dator_drag == 2:
        dator_drag = "Sax"
    else:
        dator_drag = "Påse"
    print(f"{datornamn} spelar: {dator_drag}") #skriver datorns drag
    if drag == "Sten": #beräknar vem som vinner om spelaren spelar sten
        if dator_drag == "Sten":
            vinnare = "Oavgjort"
        elif dator_drag == "Sax":
            vinnare = spelarnamn
        else:
            vinnare = datornamn
    elif drag == "Sax": #beräknar vem som vinner om spelaren spelar sax
        if dator_drag == "Sten":
            vinnare = datornamn
        elif dator_drag == "Sax":
            vinnare = "Oavgjort"
        else:
            vinnare = spelarnamn
    else: #beräknar vem som vinner om spelaren spelar påse
        if dator_drag == "Sten":
            vinnare = spelarnamn
        elif dator_drag == "Sax":
            vinnare = datornamn
        else:
            vinnare = "Oavgjort"
    print(f"\nVinnare i spelomgång {i+1}: {vinnare}!") #skriver vem som vann
    if vinnare == spelarnamn:
        spelarpoäng += 1 #delar ut poäng till vinnaren
    elif vinnare == datornamn:
        datorpoäng += 1 #samma som ovan

print(f"SLUTRESULTAT\n{13*'='}") #skriver rubrik
if spelarpoäng > datorpoäng: #skriver spelarens poäng högst upp om den vann
    print(f"{spelarnamn}: {spelarpoäng}p")
    print(f"{datornamn}: {datorpoäng}p")
    print(f"\nVinnare: {spelarnamn}")
elif datorpoäng > spelarpoäng: #skrivers datorns poäng högst upp om den vann
    print(f"{datornamn}: {datorpoäng}p")
    print(f"{spelarnamn}: {spelarpoäng}p")
    print(f"\nVinnare: {datornamn}")
else: #skriver oavgjort om ingen vann
    print(f"\nVinnare: Oavgjort!")

print("Programmet avslutades normalt.") #skriver att programmmet avslutades normalt