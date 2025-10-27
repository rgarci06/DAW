import random

numero_secret = random.randint(1,99) # Aqui utilitzo el random.randint perque es el que fa que agafi un numero aleatori entre 1 i 99
correcte = False # Aqui dic que el numero secret es false perque en cara no l'ha encertat

while True:
    alies = input("Introdueix el teu alies: ").capitalize() # Aqui faig que l'usuari escrigui el seu alies pero que la primera lletra sigui en majuscula
    if len(alies) == 0: # Aqui faig amb el len que validi que la cadena no estigui buida i si ho esta diu que torni a posar el nom. Si esta plena continua el codi
        print("Introdueix un nom, siusplau")
        continue

    hola = print(f"Hola {alies}, ara comença el programa per desxifrar la caixa forta, bona sort! ") # Dono la benvinguda a l'usuari

    for intent in range(5): # Aqui faig que els intents tenen un rang de 5 intents
        adivinar = int(input("Escriu el numero (1 al 99, 0 per sorir) : ")) # Faig un input perque l'usuari posi el numero per desxifrar

        if adivinar == 0: # Aqui faig que si el numero que posa el 0 surti del programa dient que a encertat el numero per mostar un altre missatge
            correcte = True
            break

        if adivinar == numero_secret: # Aqui faig que si el numero que posa es el correcte mostri un missatge i surti del bucle
            correcte = True
            break

        if adivinar < numero_secret: # Aqui faig que si el numero que posa es menor que el que es digi que el numero es major
            print("El numero es major")
            print(f"Aquest es l'intent: {intent}")

        else:
            print("El numero es més petit")# Aqui faig que si el numero que posa es major que el que es digi que el numero es menor
            print(f"Aquest es l'intent: {intent}")

    if not correcte: # Aqui faig que si no encerta el codi surti aquest missatge
        print(f"Has fet tots el intents, ha saltat l'alarma!. La policia va a per tu, corre!")
        break

    if correcte:
        print("Correcte, has desbloquejat la caixa forta!")
        break

    if adivinar == 0: # I per ultim que si el numero que posa es 0 surti del programa amb un misstge
        print(f"Adeu {alies}, t'ho has pensat millor i no vols problemes amb el banc Sabadell")
        break