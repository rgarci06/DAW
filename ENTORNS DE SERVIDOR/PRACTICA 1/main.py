from cc_GarciaRaúl import CompteCorrent

def main():
    print("--- CREAR COMPTE CORRENT ---")
    dni = input("Introdueix el DNI: ")
    nom = input("Introdueix el nom: ").capitalize()
    cognoms = input("Introdueix els cognoms: ").capitalize()
    saldo_inicial = float(input("Introdueix el saldo inicial (€): "))

    compte = CompteCorrent(dni, nom, cognoms, saldo_inicial)

    while True:
        print("\n--- MENÚ ---")
        print("1. Ingressar diners")
        print("2. Retirar diners")
        print("3. Veure saldo")
        print("4. Veure dades del compte")
        print("5. Sortir")

        opcio = input("Escull una opció: ")

        match opcio:
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

if __name__ == "__main__":
    main()
