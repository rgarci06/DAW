from cc_GarciaRaúl import CompteCorrent # Aqui importo la classe del meu arxiu per poderla executar aqui

def main(): # Defineixo una variable main amb el que vull que s'executi
    # Aqui faig prints perque l'usuari ompli els camps que demana
    print("--- CREAR COMPTE CORRENT ---")
    dni = input("Introdueix el DNI: ")
    nom = input("Introdueix el nom: ").capitalize()
    cognoms = input("Introdueix els cognoms: ").capitalize()
    saldo_inicial = float(input("Introdueix el saldo inicial (€): "))

    compte = CompteCorrent(dni, nom, cognoms, saldo_inicial) # Això es el que vull que l'usuari ompli

    while True: # Aqui faig un bucle per quan l'usuari fa la seva compte
        # Aquests son les opcions que té l'usuari quan a fet la seva compte 
        print("\n--- MENÚ ---")
        print("1. Ingressar diners")
        print("2. Retirar diners")
        print("3. Veure saldo")
        print("4. Veure dades del compte")
        print("5. Sortir")

        opcio = input("Escull una opció: ")
        # Aqui faig un match perque a cada una de les opcions que pot fer l'usuari
        match opcio:
            case "1":
                quantitat = float(input("Quant vols ingressar (€): ")) 
                compte.ingressar(quantitat)# Per la primera opció crido a la funció de ingressar diners del altre arxiu
            case "2":
                quantitat = float(input("Quant vols retirar (€): "))
                compte.retirar(quantitat) # Per la segona opció crido a la funcio de retirar fons del altre arxiu
            case "3":
                compte.veure_saldo() # Per la tercera opció crido a la funció de veure el saldo de l'usuari del altre arxiu
            case "4":
                compte.veure_dades() # Per la quarta funció crido a la funció de veure les dades del compte del altre arxiu
            case "5":
                print("Sortint del compte...") # Per la quinta opció es per sorir i dona un missatge
                break
            case _: # I aqui si l'usuari posa una opció surt un missatge
                print("Opció no vàlida. Torna-ho a provar.")

if __name__ == "__main__": # Amb això executo aquest arxiu
    main()
