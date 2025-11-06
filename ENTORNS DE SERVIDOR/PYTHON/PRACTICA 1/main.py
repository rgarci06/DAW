from cc_GarciaRaúl import CompteCorrent # Aqui importo la classe del altre arxiu per poderla executar aqui

def main(): # Defineixo la funció principal amb tot el codi dins
    while True: # Amb aquest bucle puc fer que l'usuari pugui fer mes comptes quan surti del programa
        print("\n--- CREAR COMPTE CORRENT ---")
        while True:
            dni = input("Introdueix el DNI amb 8 números i una lletra en MAJÚSCULA: ").strip()
            # Aqui valido la longitud dels numeros del DNI i que els 8 primers siguin numeros i que l'ultim caracter sigui una lletra majuscula.
            if len(dni) == 9 and dni[:8].isdigit() and dni[8].isalpha() and dni[8].isupper():
                break
            else:
                print("DNI incorrecte. Torna-ho a provar.")
        nom = input("Introdueix el nom: ").capitalize()
        cognoms = input("Introdueix els cognoms: ").title()
        saldo_inicial = float(input("Introdueix el saldo inicial (€): "))

        compte = CompteCorrent(dni, nom, cognoms, saldo_inicial) # Això es el que vull que l'usuari ompli

        while True: # Aixo es el menu amb les opcions que té l'usuari
            print("\n--- MENÚ ---")
            print("1. Ingressar diners")
            print("2. Retirar diners")
            print("3. Veure saldo")
            print("4. Veure dades del compte")
            print("5. Sortir")
            opcio = input("Escull una opció: ")

            match opcio: # Aixo es un cas per a cada opcio del menu
                case "1":
                    quantitat = float(input("Quant vols ingressar (€): ")) 
                    compte.ingressar(quantitat)
                case "2":
                    quantitat = float(input("Quant vols retirar (€): "))
                    compte.retirar(quantitat)
                case "3":
                    compte.veure_saldo()
                case "4":
                    compte.veure_dades()
                case "5":
                    print("Sortint del compte...")
                    break
                case _:
                    print("Opció no vàlida. Torna-ho a provar.")
        # Pregunto si l'usuari vol crear una altra compte
        resposta = input("Vols crear una altra compte? (s/n): ").strip().lower()
        if resposta != "s":
            print("Fi del programa.")
            break

if __name__ == "__main__": # Amb això executo aquest arxiu
    main()
